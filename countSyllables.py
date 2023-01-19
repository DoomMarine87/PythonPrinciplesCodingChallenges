"""Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single 
word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2."""

def count(string):
    count = 0
    for c in string:
        if c == "-":
            count +=1

    return count + 1

print(count("ho-tel"))

"""# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))"""
