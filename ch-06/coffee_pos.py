from transactions import *
import promotion
import starbuzz

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True
while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        new_price = promotion.discount(prices[choice - 1])
        if input("Starbuzz card? ").upper() == "Y":
            new_price = starbuzz.discount(new_price)
        save_transaction(new_price, credit_card, items[choice - 1])
