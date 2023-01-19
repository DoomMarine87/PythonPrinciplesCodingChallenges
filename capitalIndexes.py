"""Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should 
return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]."""

def capital_indexes(string):
    newList = []
    counter = 0

    for i in string:
        i = ord(i)
        if i >= 65 and i <= 90:
            newList.append(counter)
        counter +=1
    return newList
            


print(capital_indexes("HeLlO"))