"""Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000"."""

def format_number(num):
    num = str(num) # convert num which is an integer to a string
    numList = [] # create the list that the string will be constructed from
    
    for i in num:
        numList.append(i)
    numList.reverse() # populate numList with the string provided by user calling function and reverse it in preparation for adding ","

    listIncrease = 0
    if len(numList) > 6:
        listIncrease = (len(numList) // 3) - 1 # create listIncrease increment which is used in the next for loop.  
        # when the len is over 6 the increment neds to be calculated and this is done by dividing(int) len numList and then minusing
        #this total by one.

   
    for i in range(3, len(numList) + listIncrease, 4):
        if len(numList) > 3:
            numList.insert(i, ",")
    numList.reverse()

    res = "".join(numList)

    return res

print(format_number(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))

"""# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)"""

