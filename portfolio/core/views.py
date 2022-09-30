from django.shortcuts import render

# Create your views here.
def template_view(request):
    return render(request,template_name='base.html')