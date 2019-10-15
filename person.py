class Person:
  def __init__(self, name, job='', frequency=1, unavailable=[]):
    self.name = name
    self.job = job
    self.frequency = frequency
    self.unavailable = unavailable
    self.reduced_by = 0
  def __eq__(self, other):
    return self.name == other.name
  def __hash__(self):
    return hash(self.name)
  def __repr__(self):
    return self.name
  def actual_frequency(self):
    return self.frequency - self.reduced_by
