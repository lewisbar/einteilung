import keys

def print_perms(perms):
    '''Print permutations. Not used at the moment'''
    for perm in perms:
      for person in perm:
        print(person.name)
      print('')
  
def compile(jobs, events):
    '''Transform to a nested list based on days instead of tasks.'''
    days = []
    for event in range(events):
      day = []
      for job in jobs:
        day.append(job.perms[job.selected_perm][event])
      days.append(day)
    return days

def generate_output(jobs, events):
    '''Generate output'''
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
