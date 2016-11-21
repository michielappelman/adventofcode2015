#!/usr/bin/env python3

"""Day 13: Knights of the Dinner Table."""

import re
import itertools

FILE = 'day13_seating_input.txt'
TASK_2 = True

preferences = {}
guests = []


def pairwise(iterable):
    """From the itertools toolbox."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

# Populate the preferences
with open(FILE, 'r') as f:
    for line in f:
        pattern = r'^(.*?) would (.*?) (\d+) .* (.*).$'
        result = re.match(pattern, line)
        name1, effect, value, name2 = result.groups()
        if name1 not in guests:
            guests.append(name1)
        # make the value an integer and negative if they lose happiness
        value = int(value)
        if effect == "lose":
            value = value * -1
        preferences[name1 + name2] = value

# for the second part, add me and my (non-)preference
if TASK_2:
    for guest in guests:
        preferences[guest + "Mike"] = 0
        preferences["Mike" + guest] = 0
    guests.append("Mike")

results = []
# Get all the possible permutations ...
for combi in itertools.permutations(guests):
    pairs = [] 
    # .. pair them up ..
    for pair in pairwise(combi):
        pairs.append(( pair[0], pair[1] ))
    # .. and add the first and last name to make a circle
    pairs.append((combi[0], combi[-1]))
    
    # now start adding up all the happiness
    happiness = 0
    for neighbors in pairs:
        happiness += preferences[neighbors[0] + neighbors[1]]
        happiness += preferences[neighbors[1] + neighbors[0]]
    results.append((str(combi), happiness))

print(max(results, key=lambda x: x[1]))
