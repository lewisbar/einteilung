import gspread
from oauth2client.service_account import ServiceAccountCredentials
from einteilung.classes.person import Person
from einteilung.classes.job import Job
from einteilung.keys import keys


def get_data():
  scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
  ]

  # Get credentials from keyfile
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
    keys.KEYFILE, scope)

  # Authorization and preparation: Spreadsheet
  gc = gspread.authorize(credentials)
  worksheet = gc.open(keys.SOURCE_SHEET).sheet1

  return worksheet.get_all_values()


def get_dates(data, month=0):  # If no month is specified, take all dates
  dates = []
  for row in data[3:]:
    date = row[0]
    if month == 0 or date.endswith('.{}.'.format(str(month))):
      dates.append(date)
  return dates


def get_people(data, month=0):  # If no month is specified, take all dates
  people = []
  for col in range(1, len(data[0])):
    unavailable = []
    for row in range(len(data)):
      if (month == 0 or data[row][0].endswith('.{}.'.format(str(month)))) and data[row][col].lower() == 'x':
        unavailable.append(row - 3)
    people.append(Person(
        data[0][col].strip(), 
        data[1][col].strip(),
        int(data[2][col].strip()),
        unavailable))

  return people


def create_jobs(people):
  jobs = []
  for person in people:
    for i, job in enumerate(jobs):
      if person.job == job.title:
        jobs[i].people.append(person)
        break
    else:
      jobs.append(Job(person.job, [person]))
  return jobs


if __name__ == '__main__':
  data = get_data()
  dates = get_dates(data)
  peeps = get_people(data)
  jobs = create_jobs(peeps)
  
  print(jobs)
  print(peeps)
  print(dates)

