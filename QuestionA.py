#!/usr/bin/env python3

def doesOverlap(x1, x2, x3, x4):
    (x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
    (x3, x4) = (x3, x4) if x3 < x4 else (x4, x3)
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