#!/usr/bin/env python3
import itertools

eggnog = 150
puzzle_input = """43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38"""
containers = [ int(line) for line in puzzle_input.split()]

def combo_list(length:int) -> list:
    i = 0
    while i < 2**length:
        yield [ int(combo) for combo in list(format(i, '0{}b'.format(length))) ]
        i += 1

def get_valid_combinations(eggnog:int, containers:list) -> list:
    combinations = []
    for combo in combo_list(len(containers)):
        container_combo = list(itertools.compress(containers, combo))
        if sum(container_combo) == eggnog:
            combinations.append(container_combo)
    return combinations

def main():
    combinations = get_valid_combinations(eggnog, containers)
    combinations.sort(key=len)
    right_combinations = [ c for c in combinations 
                            if len(c) == len(combinations[0]) ]

    print("Total: {}, Minimum: {}.".format(len(combinations), 
                                           len(right_combinations)))
    # Total: 1638, Minimum: 17.

if __name__ == "__main__":
    main()
