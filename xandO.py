"""Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. If the count isn't the same, it should return False. 
If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number 
of characters."""

def x_and_o(string):
    x = 0
    o = 0

    for c in string:
        if c == "x":
            x += 1
        elif c == "o":
            o += 1
    
    if x == o:
        return True
    else:
        return False
    
print(x_and_o("xxoo"))
