"""Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise."""
def triple_and(arg1, arg2, arg3):
    bool(arg1), bool(arg2), bool(arg3)
    if arg1 and arg2 and arg3 == True:
        return True
    else:
        return False

print(triple_and("b", "b", "b"))


"""def triple_and(a, b, c):
    return a and b and c"""