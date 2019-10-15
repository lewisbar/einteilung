class Job:
  def __init__(self, title, people):
    self.title = title
    self.people = people
    self.perms = []
    self.selected_perm = 0
  def __repr__(self):
    return self.title
