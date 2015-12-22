#!/usr/bin/env python3

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def house_with_presents(presents):
    house = 1
    while not sum(factors(house))*10 >= presents:
        house += 1
    return house

def lazy_house_with_presents(presents):
    house = 1
    visits = {}
    while True:
        lazy_house_factors = []
        house_factors = factors(house)
        for factor in house_factors:
            if factor not in visits:
                visits[factor] = 1
            else:
                visits[factor] += 1
            if visits[factor] < 49:
                lazy_house_factors.append(factor)
            if sum(lazy_house_factors)*11 >= presents:
                return house
        house += 1

print(house_with_presents(34000000))
print(lazy_house_with_presents(34000000))