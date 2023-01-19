"""Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100."""

"""def largest_difference(listN):
    return max(listN) - min(listN)
    
print(largest_difference([1,2,3]))


def largest_difference(listN):
    highest = 0
    lowest = 0
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(len(listN) - 1):
            if listN[i] < listN[i + 1]:
                swapped = True
                listN[i], listN[i +1] = listN[i +1], listN[i]
    return (highest + listN[0]) - (lowest + listN[-1])

print(largest_difference([1, 2, 3]))"""

# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    return largest - smallest

print(largest_difference([3, 2, 3]))
