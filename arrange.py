from itertools import permutations, combinations
from person import Person
# from job import Job
import readdata as rd
import keys


# Find and fill gaps
def impossible_events(people, events):
  imp = 0
  for e in range(events):
    if all([e in p.unavailable for p in people]):
      imp += 1
  return imp

def deficiancy(people, events):
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
  # Reduce frequency of the person most appropriate person by 1
  for i in range(amount):
    most_frequent(people).reduced_by += 1

def find_and_fill_gaps(people, events):
  # Main gap filler function
  defic = deficiancy(people, events)
  impossible = impossible_events(people, events)

  if defic < 0:
    reduce_frencencies(people, -defic)
  if impossible > 0 and defic <=0:
    reduce_frencencies(people, impossible)

  gap = 0
  if defic > 0:
    gap += defic
  if defic < 0:
    gap += impossible

  people.append(Person('---', frequency=gap))
  return people


# Take everyone as often as they want
def multiply_by_frequency(people):
  mult = []
  for person in people:
    for i in range(person.actual_frequency()):
      mult.append(person)
  return mult

# Only allow people who are available
def filter_available(perms, tolerance=0):
  '''If there are no good perms, accept perms that have one unavailable person in it
  (or more, if necessary), and replace these people with the placeholder person.'''
  good_perms = []
  bad = 0
  for i, perm in enumerate(perms):
    good = True
    for j, person in enumerate(perm):
      if j in person.unavailable:
        permlst = list(perm)
        permlst[j] = Person('---')
        perms[i] = tuple(permlst)
        bad += 1
        if bad > tolerance:
          good = False
          break
    if good:
      good_perms.append(perm)

  if not good_perms:
    return filter_available(perms, tolerance+1)

  return good_perms


# Create ranking
def rank_frequencies(perm):
  '''Does not make sense at the moment, as all perms that contain unavailability
  get eliminated and all permutations use the same frequencies, so all perms will get the same rank.'''
  score = 0
  for person in perm:
    score -= person.reduced_by
  return score

def rank_distances(perm):
  score = 0
  for person in list(set(perm)):
    if person.actual_frequency() <=1:
      continue
    optimal_distance = len(perm) / person.actual_frequency()

    # Calculate distances
    indices = []
    for i, p in enumerate(perm):
      if p == person:
        indices.append(i)
    for i in range(len(indices)-1):
      dist = indices[i+1] - indices[i]
      score -= abs(optimal_distance - dist)
  return score

# Main distribution function for one task
def distribute(people, events):
  people_prepped = find_and_fill_gaps(people, events)

  people_prepped = multiply_by_frequency(people_prepped)

  dist = list(permutations(people_prepped))

  # Remove duplicates
  dist = list(set(dist))

  dist = filter_available(dist)

  dist = sorted(dist, key=lambda perm: rank_distances(perm), reverse=True)

  return dist


# Transform to a nested list based on days instead of tasks.
def compile(jobs, events):
  days = []
  for event in range(events):
    day = []
    for job in jobs:
      day.append(job.perms[job.selected_perm][event])
    days.append(day)
  return days

def is_free_of_conflicts(days):
  ''' No longer used '''
  for day in days:
    # Remove gap fillers before check
    condensed = list(filter(lambda p: p.name != '---', day))
    # Check for duplicates (same person, same day)
    if len(set(condensed)) != len(condensed):
      return False
  return True

def conflicting(jobs):
  conflicts = []
  combs = combinations(range(len(jobs)), 2)
  for comb in combs:
    for day in range(len(jobs[0].perms[0])):
      job1 = jobs[comb[0]]
      job2 = jobs[comb[1]]
      person1 = job1.perms[job1.selected_perm][day]
      person2 = job2.perms[job2.selected_perm][day]
      if person1.name != '---' and person1 == person2:
        conflicts.append((job1, job2))
  return conflicts

def resolve(jobs, conflicts):
  conflicts = list(set(conflicts))
  for conflict in conflicts:
    job1 = conflict[0]
    job2 = conflict[1]
    combs = []
    emergency_perms = []
    for i in range(len(job1.perms)):
      for j in range(len(job2.perms)):
        combs.append((i, j))
    # Sort combinations by desirability avoiding the worse permutations
    combs = sorted(combs, key=lambda x: (x[0] + x[1]) + abs(x[0] - x[1]))

    for comb in combs:
      job1.selected_perm, job2.selected_perm = comb[0], comb[1]
      if not (job1, job2) in conflicting(jobs):
        continue
      else:
        # Collect emergency perms in case there is no perfect perm
        emergency_perms.append((comb, len(conflicting(jobs))))

    # Pick the perm with the least number of conflicts
    best = sorted(emergency_perms, key=lambda x: x[1])[0][0]
    job1.selected_perm, job2.selected_perm = best[0], best[1]

  unresolved = conflicting(jobs)
  return unresolved


# Print permutations. Not used at the moment
def print_perms(perms):
  for perm in perms:
    for person in perm:
      print(person.name)
    print('')


# Main function for one month
def start(jobs, events):
  # Create perms for all tasks
  for job in jobs:
    job.perms = distribute(job.people, len(events))

  conflicts = conflicting(jobs)
  unresolved = resolve(jobs, conflicts)
  return unresolved


# Generate output
def generate_output(jobs, events):
  days = compile(jobs, len(events))
  out = ''
  for i, day in enumerate(days):
    out += events[i] + '\n'
    for i, person in enumerate(day):
      job = jobs[i].title
      if not (person.name == '---'  and (job != 'Leitung' and job != 'Tontechnik')):
        out += '{}: {}\n'.format(job, person.name)
    out += '\n'
  return out.strip()


def write(output):
  with open(keys.RESULTS_FILE, 'w+') as f:
    f.write(output)


def main():
  data = rd.get_data()
  unresolved = []
  outputs = []
  for month in range(1, 13):
    events = rd.get_dates(data, month)
    if not events:
      continue
    people = rd.get_people(data, month)
    jobs = rd.create_jobs(people)

    new_unresolved = start(jobs, events)
    if new_unresolved:
      unresolved.append(new_unresolved)
    outputs.append(generate_output(jobs, events))

  output = '\n\n'.join(outputs)
  write(output)
  log = output

  if unresolved:
    log += '\n\nUnresolved conflicts:' + str(len(unresolved))
    for c in unresolved:
      log += '\n' + str(*c)
    print('')
    print(log)


if __name__ == '__main__':
  main()
