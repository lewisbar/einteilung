import arrange
import publish
import event_deleter

START = ('s - Start arrangement', arrange.main)
PUBLISH = ('p - Publish arrangement', publish.main)
DELETE = ('d - Delete events from test calendar', event_deleter.main)
QUIT = ('q - Quit', exit)

def main():
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
  main()