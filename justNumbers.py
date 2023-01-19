"""Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the same order."""

def just_numbers(list):
    new_list = []
    for i in list:
        if type(i) == int:
            new_list.append(i)
    return new_list

print(just_numbers([1, "hello", 2, "my name is", 3, "simon!"]))