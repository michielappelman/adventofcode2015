#!/usr/bin/env python3
import timeit
from itertools import groupby

def say(input, n):
    input = output
    for _ in range(n):
        say = ""
        repeats = [list(g) for k, g in groupby(str(input))]
        for group in repeats:
            say += str(len(group)) + str(group[0])
        input = say
    return len(say)

print(timeit.timeit('say("1321131112", 40)', setup='from __main__ import say', number=1))
print(timeit.timeit('say("1321131112", 50)', setup='from __main__ import say', number=1))
