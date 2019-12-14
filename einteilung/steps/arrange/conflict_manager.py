from itertools import combinations

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
          # TODO: Seems to me like the perfect perm is never used, but only the best emergency perm. This should be tested.
        else:
          # Collect emergency perms in case there is no perfect perm
          emergency_perms.append((comb, len(conflicting(jobs))))

      # Pick the perm with the least number of conflicts
      best = sorted(emergency_perms, key=lambda x: x[1])[0][0]
      job1.selected_perm, job2.selected_perm = best[0], best[1]

    unresolved = conflicting(jobs)
    return unresolved
