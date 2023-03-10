"""The goal of this challenge is to analyze a binary string conssting of only zeros and ones. Your code should find the biggest 
number of consecutive zeros in the string. For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should
return the number described above."""

def consecutive_zeros(bin):
    c = 0
    cList = []
    if bin == "0":
        return 1
    
    if bin == "1":
        return 0
        
    for i in bin:
        if i == "0":
            c += 1
        elif i == "1":
            cList.append(c)
            c =  0
    
    cList.sort()
    return cList[-1]

print(consecutive_zeros("1001101000110"))

"""def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])"""
