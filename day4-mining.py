#!/usr/bin/env python3
from hashlib import md5


def brute(base, lead):
    i = 1
    while md5(bytes(base, 'utf-8')+bytes(str(i), 'utf-8')).hexdigest().startswith(lead) == False:
        i += 1
    return(i)

print(brute("ckczppom", "00000"))
print(brute("ckczppom", "000000"))
