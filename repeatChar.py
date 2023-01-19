"""Create a Python function that accepts a string. The function should return a string, with each character in the original 
string doubled. If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should 
return "112233aa!!"."""

def repeat_chars(string):
    new_string = ""
    for l in string:
        new_string += l * 2
    return new_string

print(repeat_chars("123a!"))