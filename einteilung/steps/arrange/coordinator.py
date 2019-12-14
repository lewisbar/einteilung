from einteilung.steps import readdata as rd
from itertools import permutations
from einteilung.steps.arrange import output_helper as out
from einteilung.steps.arrange import conflict_manager as confl
from einteilung.steps.arrange import gaps_and_frequencies as gaps
from einteilung.steps.arrange import evaluator

def arrange_task(people, events):
    '''Main function for one task'''
    people_prepped = gaps.find_and_fill_gaps(people, events)

    people_prepped = gaps.multiply_by_frequency(people_prepped)

    dist = list(permutations(people_prepped))

    # Remove duplicates
    dist = list(set(dist))

    dist = evaluator.filter_available(dist)

    dist = sorted(dist, key=lambda perm: evaluator.rank_distances(perm), reverse=True)

    return dist

def arrange_month(jobs, events):
    '''Main function for one month'''
    # Create perms for all tasks
    for job in jobs:
        job.perms = arrange_task(job.people, len(events))

    conflicts = confl.conflicting(jobs)
    unresolved = confl.resolve(jobs, conflicts)
    return unresolved

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

        new_unresolved = arrange_month(jobs, events)
        if new_unresolved:
            unresolved.append(new_unresolved)
            outputs.append(out.generate_output(jobs, events))

    output = '\n\n'.join(outputs)
    out.write(output)
    log = output

    if unresolved:
        log += '\n\nUnresolved conflicts:' + str(len(unresolved))
        for c in unresolved:
            log += '\n' + str(*c)
        print('')
        print(log)


if __name__ == '__main__':
  main()
