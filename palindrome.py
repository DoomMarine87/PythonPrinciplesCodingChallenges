"""A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if 
the string is a palindrome, and False otherwise."""

def palindrome(string):
    newWord = string[::-1]
    return newWord == string
    
print(palindrome("abcd"))


exp = "abcd"
newExp = exp.reversed()

print(newExp)


