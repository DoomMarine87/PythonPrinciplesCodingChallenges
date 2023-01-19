
def fizzBuzz():

    fizzBuzz = []

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzz.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzz.append("Fizz")
        elif i % 5 == 0:
            fizzBuzz.append("Buzz")
        else:
            fizzBuzz.append(str(i))
    
    return ", ".join(fizzBuzz)

print(fizzBuzz())