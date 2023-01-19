"""Write a function in Python that accepts a credit card number. It should return a string where all the characters 
are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it 
should return "4444"."""

def credit_card_hide(n):
    n = str(n)
    for n in n[-4:]:
        print(n, end="")

credit_card_hide(4444444444444444)

