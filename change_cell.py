# This is primarily meant to be used in Pythonista on iPhone,
# because the Google Spreadsheets mobile app doesn't allow multiline input.
# It won't work as expected if the command line doesn't accept
# multiline input, like Pythonista does.

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import keys

scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive'
]

# Get credentials from keyfile
credentials = ServiceAccountCredentials.from_json_keyfile_name(
  keys.KEYFILE, scope)

# Authorization and preparation: Spreadsheet
gc = gspread.authorize(credentials)

cell_pos = input('Enter cell position (for example, B3):\n')
content = input('\nEnter new cell content:\n')

if input('\nTest or real? (t/r)') == 'r':
  print('\nWriting to spreadsheet ...')
  worksheet = gc.open(keys.REAL_SHEET).sheet1
else:
  print('\nWriting to spreadsheet ...')
  worksheet = gc.open(keys.TEST_SHEET).sheet1

worksheet.update_acell(cell_pos, content)
print('\n{} updated with\n"{}"\nin spreadsheet\n"{}".'.format(cell_pos, content, worksheet.spreadsheet.title))
