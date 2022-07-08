""" Find smallest and second smallest in an array with duplicate elements"""
# remove duplicate elements from the array
def minAnd2Min(a,n):
    a = list(set(a))
    a.sort()
    if len(a) == 1:
        return [-1]
    else:
        return [a[0],a[1]]

