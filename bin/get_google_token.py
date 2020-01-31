#!/usr/bin/env python3

import os

from dotenv import load_dotenv
load_dotenv()

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main():
    flow = InstalledAppFlow.from_client_config({
        "installed": {
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET")
        }
    }, SCOPES)
    creds = flow.run_local_server(port=0)

    print("GOOGLE_REFRESH_TOKEN=" + creds.refresh_token)

if __name__ == '__main__':
    main()
