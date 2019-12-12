from person import Person

def filter_available(perms, tolerance=0):
    '''Only allow perms where people aren't in places where they are unavailable.
    If there are no good perms, accept perms that have one unavailable person in it
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

def rank_frequencies(perm):
    '''Does not make sense at the moment, as all perms that contain unavailability
    get eliminated and all permutations use the same frequencies, so all perms will get the same rank.'''
    score = 0
    for person in perm:
      score -= person.reduced_by
    return score
