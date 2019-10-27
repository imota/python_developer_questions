#!/usr/bin/env python3

def does_overlap(line1, line2):
    (x1, x2) = (line1[0], line1[1]) if line1[0] < line1[1] else (line1[1], line1[0])
    (x3, x4) = (line2[0], line2[1]) if line2[0] < line2[1] else (line2[1], line2[0])
    if x3 > x1 and x3 < x2:
        return True
    if x4 > x1 and x4 < x2:
        return True
    if x1 > x3 and x1 < x4:
        return True
    if x2 > x3 and x2 < x4:
        return True
    if (x1 == x3) and (x2 == x4):
        return True
    return False