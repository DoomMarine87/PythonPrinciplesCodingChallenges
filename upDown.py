"""Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two 
numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6)."""

def up_down(number):
    up = number + 1
    down = number - 1
    return (down, up)

print(up_down(5))

"""def up_down(x):
    return (x-1, x+1)"""