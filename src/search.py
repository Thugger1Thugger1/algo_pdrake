
# Best: 1
# Average: n
# Amort: n   (n/2)
# Worst: n


def linear_search(key, ls):
    for i, x in enumerate(ls):
        if x == key:
            return i
    return -1


# Best: 1
# Average: log(n)
# Amort: log(n)
# Worst: log(n)

def binary_search(key, ls):
    lo = 0
    hi = len(ls) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < ls[mid]:
            hi = mid - 1
        elif key == ls[mid]:
            return mid
        else:
            lo = mid + 1
    return -1


#assumes all floating point numbers that are evenly distributed
# Best: 
# Average: log(log(n))
# Amart: 
# Worst: n


def interpolation_search(key, ls):
    lo = 0
    hi = len(ls) - 1
    while lo <= hi:
        if lo == hi:
            if key == ls[lo]:
                return lo
            else:
                return -1
        fraction = (key - ls[lo]) / (ls[hi] - ls[lo])
        mid = int(lo + (hi - lo) * fraction)
        mid = max(lo, min(hi, mid))  # Because the formula could produce a value out of this range
        if key < ls[mid]:
            hi = mid - 1
        elif key == ls[mid]:
            return mid
        else:
            lo = mid + 1
    return -1
