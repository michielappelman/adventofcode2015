#!/usr/bin/env python3

"""Day 11: Corporate Policy."""

import re

# INPUT = "hxbxwxba"
INPUT = "hxbxxyzz"

SANTA_CHARS = "abcdefghijklmnopqrstuvwxyz"
BASE_CHARS = "0123456789ABCDEFGHIJKLMNOP"
TRANS_TO = str.maketrans(SANTA_CHARS, BASE_CHARS)
TRANS_FROM = str.maketrans(BASE_CHARS, SANTA_CHARS)

rules = []


def rule(rule_test):
    rules.append(rule_test)
    return rule_test


@rule
def rule_1(pw):
    numerics = [ord(c) for c in pw]
    for index, number in enumerate(numerics):
        try:
            if (numerics[index + 1] == number + 1 and
                    numerics[index + 2] == number + 2):
                return True
        except IndexError:
            pass
    return False


@rule
def rule_2(pw):
    for c in "iol":
        if c in pw:
            return False
    return True


@rule
def rule_3(pw):
    if re.search(r'(\w)\1.*(\w)\2', pw):
        return True
    else:
        return False


def to_base(num, b, numerals=BASE_CHARS):
    return (((num == 0) and numerals[0]) or
            (to_base(num // b, b, numerals).lstrip(numerals[0]) +
                                                   numerals[num % b]))


def increment(word):
    base = word.translate(TRANS_TO)
    base_26 = int(base, 26) + 1
    while True:
        incremented = to_base(base_26, 26).translate(TRANS_FROM)
        yield incremented
        base_26 += 1


def find_next_password(current):
    for password in increment(current):
        if all([r(password) for r in rules]):
            return password

print(find_next_password(INPUT))
