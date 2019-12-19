# einteilung
Makes a plan which volunteer musicians/sound guys are in charge at which date in our church service

The program reads its data (which people, jobs and events are there;
who can do which jobs, wants to play how often and is unavailable at which dates)
from a google spreadsheet.
Then it divides the event list into months, creates every possible arrangement, and picks the best possibility.
There should only be 4-5 events per months, or maybe 7 at most. If you have more, there are too many possible permutations.
10 events mean 10! (10\*9\*8\*7\*6\*5\*4\*3\*2\*1) possibilities per job. That's a big number.
That's why the input is divided into months. I typically do this once every three months. That's about 13 sundays.
Finding every possible arrangement for 13 events would be too much, but for each month individually (4-5 sundays),
it works great.
When the arrangement is done, you have the option to publish it to a google spreadsheet and a google calendar.

Actually, I think that in its current state, this program is too special to be used by anyone else.
The input spreadsheet has to be in a certain format, and the output spreadsheet as well, and
our church situation might also be a special use case.
Still, feel free to ask if you need help.

It needs a Google API JSON key file to work, and a file 'keys.py' with confidental data.

The file 'keys.py' must contain these constants: 

KEYFILE = '[google api key file].json'

REAL_SHEET = '[name of the official output spreadsheet]'

TEST_SHEET = '[name of a test output spreadsheet]'

REAL_CAL = '[ID of the official calendar]'

TEST_CAL = '[ID of a test calendar]'

RESULTS_FILE = '[name of the file to which the results are written, and later read from; can be any name]'

EVENT_NAME = '[how the calendar events should be named; will be followed by the name of the sound guy]'

LOCATION = '[location for the calendar events]'

START = '[start time for calendar events, for example 08:30:00]'

END = '[end time for calendar events, for example 12:00:00]'

ZONE = '[time zone for calendar events, for example Europe/Berlin]'

SOURCE_SHEET = '[name of the input spreadsheet]'
