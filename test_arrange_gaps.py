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
    ]
    return people[:amount]

def mock_people_unavailable(amount):
    people = [
        Person('Person 1', job='Job 1', frequency=1, unavailable=[0,1,2]),
        Person('Person 2', job='Job 2', frequency=1, unavailable=[0,1,2]),
        Person('Person 3', job='Job 3', frequency=1, unavailable=[0,1,2]),
        Person('Person 4', job='Job 1', frequency=1, unavailable=[0,1,2]),
        Person('Person 5', job='Job 2', frequency=1, unavailable=[0,1,2]),
        Person('Person 6', job='Job 3', frequency=1, unavailable=[0,1,2]),
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
    
def test_deficiancy_unavailable():
    '''People are all available as often as their frequencies'''
    assert gaps.deficiancy(mock_people_unavailable(5), 8) == 3

def test_deficiancy_unavailable_overload():
    '''People are available less often than their frequencies. The deficiancy function should ignore availability. There are other functions for that.'''
    assert gaps.deficiancy(mock_people_unavailable(5), 5) == 0