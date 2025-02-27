from io import open
import time
from random import randrange


def get_price():

    # start_of_price = 247
    # end_of_price = 251
    with open("beansrus.html", "r") as page:
        text = page.read()
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])
    price += randrange(-10, 20)/10
    print(f'{"."*5} {price}')
    return price


price = 99.99
while price > 4.74:
    time.sleep(1)
    price = get_price()
print(f"Buy at {price}")
