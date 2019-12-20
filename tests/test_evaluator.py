from einteilung.steps.arrange import evaluator as ev
from einteilung.classes.person import Person

def mock_perms(p1, p2, p3):
    return [(p1, p2, p3), (p1, p3, p2), (p2, p1, p3), (p2, p3, p1), (p3, p1, p2), (p3, p2, p1)]

# p1
def test_filter_available_p1_beginning():
    p1 = Person("Person 1", unavailable=[0])
    p2 = Person("Person 2")
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p2, p1, p3), (p2, p3, p1), (p3, p1, p2), (p3, p2, p1)]  # p1 never at index 0

def test_filter_available_p1_middle():
    p1 = Person("Person 1", unavailable=[1])
    p2 = Person("Person 2")
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p1, p3, p2), (p2, p3, p1), (p3, p2, p1)]  # p1 never at index 1

def test_filter_available_p1_end():
    p1 = Person("Person 1", unavailable=[2])
    p2 = Person("Person 2")
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p1, p3, p2), (p2, p1, p3), (p3, p1, p2)]  # p1 never at index 2


# p2
def test_filter_available_p2_beginning():
    p1 = Person("Person 1")
    p2 = Person("Person 2", unavailable=[0])
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p1, p3, p2), (p3, p1, p2), (p3, p2, p1)]  # p2 never at index 0

def test_filter_available_p2_middle():
    p1 = Person("Person 1")
    p2 = Person("Person 2", unavailable=[1])
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p3, p2), (p2, p1, p3), (p2, p3, p1), (p3, p1, p2)]  # p2 never at index 1

def test_filter_available_p2_end():
    p1 = Person("Person 1")
    p2 = Person("Person 2", unavailable=[2])
    p3 = Person("Person 3")
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p2, p1, p3), (p2, p3, p1), (p3, p2, p1)]  # p2 never at index 2


# p3
def test_filter_available_p3_beginning():
    p1 = Person("Person 1")
    p2 = Person("Person 2")
    p3 = Person("Person 3", unavailable=[0])
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p1, p3, p2), (p2, p1, p3), (p2, p3, p1)]  # p3 never at index 0

def test_filter_available_p3_middle():
    p1 = Person("Person 1")
    p2 = Person("Person 2")
    p3 = Person("Person 3", unavailable=[1])
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p2, p3), (p2, p1, p3), (p3, p1, p2), (p3, p2, p1)]  # p3 never at index 1

def test_filter_available_p3_end():
    p1 = Person("Person 1")
    p2 = Person("Person 2")
    p3 = Person("Person 3", unavailable=[2])
    good_perms = ev.filter_available(mock_perms(p1, p2, p3))
    assert good_perms == [(p1, p3, p2), (p2, p3, p1), (p3, p1, p2), (p3, p2, p1)]  # p3 never at index 2
