import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build  # Google Calendar API
from months import months
from event import Event
from datetime import date as dt
from tqdm import tqdm
import keys


def main():
  scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/calendar'
  ]

  # Get credentials from keyfile
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
    keys.KEYFILE, scope)

  # Authorization and preparation
  gc = gspread.authorize(credentials)  # Spreadsheet
  service = build('calendar', 'v3', credentials=credentials)  # Calendar

  # Test or real?
  test_or_real = input('\nTest or real? (t/r)').lower()
  if test_or_real == 'r':
    sheetname = keys.REAL_SHEET
    calId = keys.REAL_CAL
  elif test_or_real == 't':
    sheetname = keys.TEST_SHEET
    calId = keys.TEST_CAL
  else:
    return 'Invalid input'

  # Spreadsheet or calendar?
  sheet_or_cal = input('\nWrite to spreadsheet, calendar, or both? (s/c/b)').lower()
  if sheet_or_cal not in 'scb':
    return 'Invalid input'

  # Read the data that should be applied
  with open(keys.RESULTS_FILE, 'r') as f:
    plan = f.read().strip()

  # Parsing
  events = []
  for i, day in enumerate(plan.split('\n\n')):
    lines = day.split('\n')
    date = lines[0]
    d, m = date.split('.')[:2]
    d0, m0 = ['0' + x if len(x) == 1 else x for x in [d, m]]
    musicians = '\n'.join(lines[1:-1])
    sound = lines[-1].replace('Tontechnik: ', '')
    events.append(Event(d, m, d0, m0, sound, musicians))

  # Get the newest sheet, also to be able to get the correct year
  latest_sheet = sorted(gc.open(sheetname).worksheets(), key=lambda s: s.title)[-1]
  print(latest_sheet)

  # Spreadsheet
  if sheet_or_cal in 'sb':
    tqdm.write('\nWriting to spreadsheet ...')
    worksheet = latest_sheet  # gc.open(sheetname).sheet1
    count = 0
    for e in tqdm(events):
      row = worksheet.find('So., {}. {} '.format(e.day, months[int(e.month)-1])).row
      worksheet.update_cell(row, 2, e.sound)
      worksheet.update_cell(row, 4, e.musicians)
      count += 1
    tqdm.write('{} events added.'.format(count))

  # Calendar
  if sheet_or_cal in 'cb':
    tqdm.write('\nWriting to calendar ...')
    # year = dt.today().year
    year = latest_sheet.title
    count = 0
    for e in tqdm(events):
      cal_event = {
        'summary': '{} {}'.format(keys.EVENT_NAME, e.sound),
        'location': keys.LOCATION,
        'description': e.musicians,
        'start': {
          'dateTime': '{}-{}-{}T{}'.format(year, e.month0, e.day0, keys.START),
          'timeZone': keys.ZONE,
        },
        'end': {
          'dateTime': '{}-{}-{}T{}'.format(year, e.month0, e.day0, keys.END),
          'timeZone': keys.ZONE,
        },
      }
      cal_event = service.events().insert(
        calendarId=calId, body=cal_event).execute()
      # print('Event created: {} {}'.format(event['start']['dateTime'], cal_event['summary']))
      count += 1
    tqdm.write('{} events added.'.format(count))

  tqdm.write('\nDone.\n')


if __name__ == '__main__':
  main()
