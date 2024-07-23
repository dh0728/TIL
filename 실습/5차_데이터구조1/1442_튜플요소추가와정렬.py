def sort_tuple(tup):
    tup=list(tup)
    tup.sort()
    new_tuple = tuple(tup)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
