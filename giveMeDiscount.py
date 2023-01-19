"""Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. For example, if the price is 100 and 
the discount is 20, the function should return 80."""

def give_me_disc(price, discountPercent):
    new_price = price * (discountPercent / 100)
    new_price = price - new_price
    return new_price

print(give_me_disc(100 , 20))