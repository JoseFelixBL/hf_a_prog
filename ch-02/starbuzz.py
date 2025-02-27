from io import open
import time
from random import randrange


def send_to_twitter(msg="Buy now!"):
    """This is just a mock-up function of a twitter send"""
    print(f"Sending this message to twitter: {msg}")


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


buy_now = input("Do you want to buy now? (y/n) ")
if buy_now == 'y':
    price = get_price()
    print(f"Buy NOW at {price}")
    send_to_twitter(f"Urgent buy at {price}")
else:
    price = 99.99
    while price > 4.74:
        time.sleep(1)
        price = get_price()
    print(f"Buy at {price}")
    send_to_twitter(f"Buy at good price of: {price}")
