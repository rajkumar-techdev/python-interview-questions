def find_largest(lst):
    if not lst:
        return None
    largest=lst[0]

    for num in lst:
        if largest<num:
            largest=num
    return largest

lst=[23,43,54,5,4,34,545]

print("Largest Element: ",find_largest(lst))

