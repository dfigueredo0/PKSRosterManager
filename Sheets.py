import os
from PKSRosterManager.Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/drive.file']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Create a Blank Spreadsheet
sheets_file1 = service.spreadsheets().create().execute()
print(sheets_file1)