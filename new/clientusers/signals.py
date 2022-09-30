import datetime
import json
import os

from django.db.models.signals import post_delete, post_save
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from .models import  Event

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_service(refresh=False):
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(os.environ.get("client_secret")), scopes=SCOPES
    )
    # or if you have a file
    # credentials = ServiceAccountCredentials.from_json_keyfile_name(
    #     filename="file.json", scopes=SCOPES
    # )
    service = build("calendar", "v3", credentials=credentials)
    return service


def handle_event(sender, created, instance, **kwargs):
        """this function creates the events in the google agenda and updates them if changed in the website"""
        service = get_service()
        event = instance
        if not event.end_date:
            event.end_date = event.start_date
        if not event.end_time and event.start_time:
            event.end_time = event.start_time
        elif not event.end_time:
            event.end_time = datetime.datetime.min.time()
        if not event.start_time:
            event.start_time = datetime.datetime.min.time()
        if event.end_date < event.start_date:
            event.end_date, event.start_date = event.start_date, event.end_date
        queryset = Event.objects.filter(
            id=event.id
        )  # https://stackoverflow.com/questions/1555060/how-to-save-a-model-without-sending-a-signal
        # this is used so that we can update the google event within this signal without reshooting this signal(signals shot every time an object is saved)
        event = {
            "summary": event.description,
            "location": event.location or "",
            "description": (event.description + " " + event.summary),
            "start": {
                "dateTime": datetime.datetime.combine(
                    event.start_date, event.start_time
                ).isoformat(),
                "timeZone": "Europe/Amsterdam",
            },
            "end": {
                "dateTime": datetime.datetime.combine(
                    event.end_date, event.end_time
                ).isoformat(),
                "timeZone": "Europe/Amsterdam",
            },
            "recurrence": [],
            "reminders": {},
        }

        if created or not instance.google_link:
            try:
                event = (
                    service.events()
                    .insert(
                        calendarId=os.environ.get("calendarId"),
                        body=event,
                    )
                    .execute()
                )
                queryset.update(google_link=event["id"])
            except HttpError as error:
                # print("An error occurred: %s" % error)
                pass
        else:
            try:
                event = (
                    service.events()
                    .update(
                        calendarId=os.environ.get("calendarId"),
                        body=event,
                        eventId=instance.google_link,
                    )
                    .execute()
                )
                queryset.update(google_link=event["id"])
            except HttpError as error:
                # print("An error occurred: %s" % error)
                pass
        # print("#############ADDED NEW       #############")


def delete_event(sender, instance, **kwargs):
    """this function deletes an event from google agenda when deleted in the website"""
    try:
        service = get_service()
        service.events().delete(
            calendarId=os.environ.get("CalendarId"),
            eventId=instance.google_link,
        ).execute()
    except:
        pass


post_save.connect(handle_event, sender=Event)
post_delete.connect(delete_event, sender=Event)
