"""Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True."""

def all_equal(list):

    charsSame = True
    for i in range(len(list) -1):
        if list[i]  != list[i +1]:
            charsSame = False
        else:
            charsSame = True
    return charsSame

print(all_equal([3,3,3,3,3,2,3]))

"""# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)"""