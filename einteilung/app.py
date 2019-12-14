from einteilung.steps.arrange import coordinator
from einteilung.steps import publish
from einteilung.steps import delete_events

START = ('s - Start arrangement', coordinator.main)
PUBLISH = ('p - Publish arrangement', publish.main)
DELETE = ('d - Delete events from test calendar', delete_events.main)
QUIT = ('q - Quit', exit)

def run():
  while True:
    options = [START, PUBLISH, DELETE, QUIT]
    print('')
    print(*[o[0] for o in options], sep='\n')
    inp = input().lower()
    for o in options:
      if inp == o[0][0]:
        o[1]()
        break


if __name__ == '__main__':
  run()