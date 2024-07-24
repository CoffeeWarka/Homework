from math import inf
def divide_zero(first, second):
    if second == 0:
        return inf
    else:
        divide = first/second
        return divide