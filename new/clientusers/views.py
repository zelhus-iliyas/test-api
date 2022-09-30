import httplib2
import pickle
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseRedirect)
from django.shortcuts import redirect
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from oauth2client.client import OAuth2WebServerFlow

from .models import ClientUser, Credentials


def get_flow(request):    
    flow = OAuth2WebServerFlow(
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        scope=settings.GOOGLE_SCOPE,
        redirect_uri=settings.OAUTH_REDIRECT_URI,
        access_type='offline',
        state=''
    )
    return flow


def login(request):
    next = request.GET.get('next', 'home')
    request.session['next'] = next

    if not request.user.is_authenticated():
        flow = get_flow(request)
        flow.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,request.user)
        request.session['flow'] = pickle.dumps(flow).decode('iso-8859-1')
        redirect_uri = flow.step1_get_authorize_url()
        return redirect(redirect_uri)
    else:
        return redirect(reverse_lazy(next))



def oauth2redirect(request):
    # Make sure that the request is from who we think it is
    if not xsrfutil.validate_token(settings.SECRET_KEY,
                                   request.GET.get('state').encode('utf8'),
                                   request.user):
        return HttpResponseBadRequest()

    code = request.GET.get('code')
    error = request.GET.get('error')

    if code:
        flow = get_flow(request)
        credentials = flow.step2_exchange(code)

        request.session['creds'] = credentials.to_json()
        email = credentials.id_token.get("email")
        user_exists = False
        try:
            user = ClientUser.objects.get(email=email)
            user_exists = True
        except ClientUser.DoesNotExist:
            user = ClientUser.objects.create(credentials)

        # Since we've oauth2'd the user, we should set the backend appropriately
        # This is usually done by the authenticate() method.
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        # Refresh token is needed for renewing google api access token
        if credentials.refresh_token:
            user.refresh_token = credentials.refresh_token
        user.save()

        storage = DjangoORMStorage(Credentials, 'id', user, 'credential')
        storage.put(credentials)

        # Register that the user has successfully logged in
        auth_login(request, user)

        next = request.session.get('next', reverse_lazy('/'))
        return HttpResponseRedirect(next)
    elif code is None and error:
        return HttpResponse(str(error))
    else:
        return HttpResponseBadRequest()


@login_required
def logout(request):
    user = request.user
    credentials = Credentials.objects.get(id=user.id)
    credentials.revoke(httplib2.Http())
    credentials.delete()
    storage = DjangoORMStorage(Credentials, 'id', user, 'credential')
    storage.delete()

    auth_logout(request)
    return HttpResponseRedirect('/')