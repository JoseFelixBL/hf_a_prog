from pathlib import Path


def save_transaction(price, credit_card, description):
    output_file = Path("transactions.txt")
    output_dir = Path('ch-06')
    output_final = output_dir / output_file
    with open(output_final, "a") as file:
        file.write(f"{int(price*100):07}{credit_card:16}{description:16}\n")


items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
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
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])
