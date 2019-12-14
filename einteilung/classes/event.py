class Event():
  def __init__(self, day, month, day0, month0, sound, musicians):
    self.day = day
    self.month = month
    self.day0 = day0
    self.month0 = month0
    self.sound = sound
    self.musicians = musicians
  def repr(self):
    return '{}.{}. {}\n{}'.format(self.day, self.month, self.sound, self.musicians)
