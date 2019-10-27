#!/usr/bin/env python3

def compare_strings(str1, str2):
    str1 = [int(x) for x in str1.replace(' ','').split('.')]
    str2 = [int(x) for x in str2.replace(' ','').split('.')]

    counter_limit = min(len(str1), len(str2))
    for i in range(counter_limit):
        if str1 > str2:
            return 1
        if str1 < str2:
            return -1

    if len(str1) > counter_limit:
        return 1
    if len(str2) > counter_limit:
        return -1

    return 0