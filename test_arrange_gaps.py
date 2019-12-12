from Arrange import gaps_and_frequencies as gaps
from person import Person

def mock_people(amount):
    people = [
        Person('Person 1', job='Job 1', frequency=1, unavailable=[]),
        Person('Person 2', job='Job 2', frequency=1, unavailable=[]),
        Person('Person 3', job='Job 3', frequency=1, unavailable=[]),
        Person('Person 4', job='Job 1', frequency=1, unavailable=[]),
        Person('Person 5', job='Job 2', frequency=1, unavailable=[]),
        Person('Person 6', job='Job 3', frequency=1, unavailable=[]),
        Person('Person 7', job='Job 1', frequency=1, unavailable=[]),
        Person('Person 8', job='Job 2', frequency=1, unavailable=[]),
        Person('Person 9', job='Job 3', frequency=1, unavailable=[]),
        Person('Person 10', job='Job 1', frequency=1, unavailable=[]),
        Person('Person 11', job='Job 2', frequency=1, unavailable=[]),
        Person('Person 12', job='Job 3', frequency=1, unavailable=[]),
    ]
    return people[:amount]

def test_deficiancy_2():
    '''5 events, 3 people with frequency 1, makes a deficiancy of 2'''
    assert gaps.deficiancy(mock_people(3), 5) == 2

def test_deficiancy_0():
    '''3 events, 3 people with frequency 1, makes a deficiancy of 0'''
    assert gaps.deficiancy(mock_people(3), 3) == 0

def test_deficiancy_negative_2():
    '''3 events, 5 people with frequency 1, makes a deficiancy of -2'''
    assert gaps.deficiancy(mock_people(5), 3) == -2
    