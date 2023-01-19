"""Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, 
only a, e, i, o, and u will be counted as vowels — not y."""

def vowel_counter(word):
    vc = 0

    for l in word:
        if l == "a":
            vc +=1
        elif l == "e":
            vc += 1
        elif l == "i":
            vc += 1
        elif l == "o":
            vc += 1
        elif l == "u":
            vc += 1
    
    return vc

print(vowel_counter("onomatopoeia"))
