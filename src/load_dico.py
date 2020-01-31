from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def load_dico(manulex_spreadsheet_id, refresh_token, client_id, client_secret):
    credentials = Credentials(
        None,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'],
        token_uri="https://accounts.google.com/o/oauth2/token"
    )
    service = build('sheets', 'v4', credentials=credentials)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=manulex_spreadsheet_id, range='dico manulex!A1:E').execute()
    values = result.get('values', [])

    lines = []
    def format_line(line):
        word, phonetic, blending, relations = line

        return ({
            'word': word,
            'phonetic': phonetic,
            'blending': blending.split('-'),
            'relations': relations.split('.')
        })

    lines = list(map(format_line, values[1:-1]))

    dico = { line['word']: line['relations'] for line in lines }
    return dico
