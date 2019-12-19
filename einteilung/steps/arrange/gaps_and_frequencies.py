from einteilung.classes.person import Person

def impossible_events(people, events):
    imp = 0
    for e in range(events):
        if all([e in p.unavailable for p in people]):
            imp += 1
    return imp


def deficiancy(people, events):
    '''Doesn't take availability into account. This is just a first step in the arrangement process.'''
    freqsum = sum([p.frequency for p in people])
    return events - freqsum


def most_frequent(people):
    winner = people[0]
    for person in people:
        if person.actual_frequency() > winner.actual_frequency() \
            or (person.actual_frequency() == winner.actual_frequency()
                and person.reduced_by < winner.reduced_by):
            winner = person
    return winner


def reduce_frencencies(people, amount):
    '''Reduce frequency of the person most appropriate person by 1 until the amount is used up'''
    for _ in range(amount):
        most_frequent(people).reduced_by += 1


def multiply_by_frequency(people):
    '''Take everyone as often as they want'''
    mult = []
    for person in people:
        for _ in range(person.actual_frequency()):
            mult.append(person)
    return mult


def find_and_fill_gaps(people, events):
    '''MAIN GAP FILLER FUNCTION'''
    defic = deficiancy(people, events)
    impossible = impossible_events(people, events)

    if defic < 0:
        reduce_frencencies(people, -defic)
    if impossible > 0 and defic <= 0:
        reduce_frencencies(people, impossible)

    gap = 0
    if defic > 0:
        gap += defic
    if defic < 0:
        gap += impossible

    people.append(Person('---', frequency=gap))
    return people
