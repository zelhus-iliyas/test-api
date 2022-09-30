from __future__ import print_function

import datetime
import os.path
from tracemalloc import start
from unittest import result
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/calendar"]


class Index(View):
    template = "index.html"

    def get(self, request):
        return render(request, self.template)



def GoogleCalendarInitView(request):
    """
    This Function starts the first step of OAuth2 mechanism.It Prompts the user for their creds and stores it in token.json file.
    The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
    """
    creds = None

    if os.path.exists("token.json"):

        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no credentials exists then the user will login.

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )

            creds = flow.run_local_server()

        # Now we will save the credentials for future in token.json

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return HttpResponseRedirect("/rest/v1/calendar/redirect/")


def GoogleCalendarRedirectView(request):
    """
    This Function calls The Google Calender API and lists the Upcoming events of the user (if they exists) in tabular format.
    """

    try:
        service = build(
            "calendar",
            "v3",
            credentials=Credentials.from_authorized_user_file("token.json", SCOPES),
        )

        # Calling the Google Calendar API.
        now = datetime.datetime.utcnow().isoformat() + "Z"

        print("Getting the upcoming events")

        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return HttpResponse(
                "No Upcoming Events found.Please add events in your Google Calender."
            )

        result = {}

        # Creating a dictionary to store the events and their corresponding date and time.

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            result[event["summary"]] = start

        print(result)

        return render(request, "calender.html", {"response": result})

    except HttpError as error:
        print("An error occurred: %s" % error)
