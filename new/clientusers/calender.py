from __future__ import print_function
from asyncio.windows_events import NULL

# import csv
import datetime
import os.path

# import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# from common import search_messages

# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/calendar.readonly']

def parse_parts(service, parts, folder_name, message):
    pass

# def read_message(service, message):
#     pass

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            print(start, event)
        print('events printed')
    except HttpError as error:
        print('An error occurred: %s' % error)

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        messageList=service.users().messages().list(userId='me').execute()
        # print('messageList:',messageList.get('messages'))
        f1 = open("demofile3.csv", "w",encoding="utf-8")
        mailDict = {"from" : "From", "to": "To", "subject" : "Subject"}
        mailDictArr = [mailDict]
        i=1
        mailDictArr.insert(i,mailDict)
        f1.write(mailDict["from"]+"," + mailDict["to"]+","+mailDict["subject"] + '\n')
        for message in messageList.get('messages'):
            msg = service.users().messages().get(userId='me', id=message.get('id'), format='full').execute()
            # print('msg:::',msg)
            # parts can be the message body, or attachments
            payload = msg['payload']
            headers = payload.get("headers")
            parts = payload.get("parts")
            # print('parts:::::',parts)
            if parts:
                for part in parts:
                    folder_name=''
                    filename = part.get("filename")
                    mimeType = part.get("mimeType")
                    body = part.get("body")
                    data = body.get("data")
                    file_size = body.get("size")
                    part_headers = part.get("headers")
                    if part.get("parts"):
                        # recursively call this function when we see that a part
                        # has parts inside
                        parse_parts(service, part.get("parts"), folder_name, message)
                    if mimeType == "text/plain":
                        # if the email part is text plain
                        if data:
                            text = urlsafe_b64decode(data).decode()
                            print('message decrpted:',text)
                    elif mimeType == "text/html":
                        # if the email part is an HTML content
                        # save the HTML file and optionally open it in the browser
                        folder_name = "email"
                        if not filename:
                            filename = "index-"+str(i)+".html"
                        filepath = os.path.join(folder_name, filename)
                        print("Saving HTML to", filepath)
                        with open(filepath, "wb") as f:
                            f.write(urlsafe_b64decode(data))
                    has_subject = False
                if headers:
                    # this section prints email basic info & creates a folder for the email
                    for header in headers:
                        name = header.get("name")
                        value = header.get("value")
                        if name.lower() == 'from':
                            mailDict["from"]=value
                        if name.lower() == "to":
                            mailDict["to"]=value
                        if name.lower() == "subject":
                            # make our boolean True, the email has "subject"
                            has_subject = True
                            # make a directory with the name of the subject
                            folder_name = clean(value)
                            mailDict["subject"]=value
                mailDictArr.insert(i,mailDict)
                f1.write(mailDict["from"]+"," + mailDict["to"]+","+mailDict["subject"] + '\n')
                mailDict = {"from" : "", "to": "", "subject" : ""}
                if not has_subject:
                    # if the email does not have a subject, then make a folder with "email" name
                    # since folders are created based on subjects
                    if not os.path.isdir(folder_name):
                        os.mkdir(folder_name)
                parse_parts(service, parts, folder_name, message)
                print("=" * 50)
            i=i+1           
                    # body = part.get("body")
                    # data = body.get("data")
                    # file_size = body.get("size")
                    # part_headers = part.get("headers")
                    # if mimeType == "text/plain":
                    #     # if the email part is text plain
                    #     if data:
                    #         text = urlsafe_b64decode(data).decode()
                    #         print('message decrpted:',text)





        # # get emails that match the query you specify from the command lines
        # result_message = search_messages(service, sys.argv[message.get('id')])
        # # for each email matched, read it (output plain/text to console & save HTML and attachments)
        # for msg in result_message:
        #     read_message(service, msg)

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])
        f1.close()
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
        f1.close()

if __name__ == '__main__':
    main()