"""Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself. 
One hint you get is that you'll need to use Pi in order to solve this problem. You can import the value for Pi from Python's 
math module."""

from math import pi

def radians_to_degrees(radians):
    if radians == 0:
        radians = int(input("Enter a number greater than 0: "))

    degrees = radians * 180 / pi
    return degrees

for i in range(1,6):
    print(i, "radians is equal to: ", radians_to_degrees(i), "degrees")

