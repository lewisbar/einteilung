# Deletes events from the Dev calendar.
# Currently, it's events whose summary starts with 'Godi-TT'.
# The idea is to clear out data that has been added in the development process.

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import keys


def main():
  # Preparation
  scope = [
    'https://www.googleapis.com/auth/calendar'
  ]
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
    keys.KEYFILE, scope)
  service = build('calendar', 'v3', credentials=credentials)
  calId = keys.TEST_CAL

  events = service.events().list(calendarId=calId, maxResults=9999).execute()
    # 'maxResults=9999' works around a bug that sometimes returned an empty list

  print('')
  for e in events['items']:
    if not 'summary' in e:
      continue  # There were some strange events without summary in another calendar that caused a crash.
    if e['summary'].startswith(keys.EVENT_NAME):  # Criteria for events that should be deleted
      print('Deleting event: {} {}'.format(e['start']['dateTime'], e['summary']))
      service.events().delete(calendarId=calId, eventId=e['id']).execute()


if __name__ == '__main__':
  main()