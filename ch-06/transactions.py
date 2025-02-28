from pathlib import Path


def save_transaction(price, credit_card, description):
    output_file = Path("transactions.txt")
    output_dir = Path('ch-06')
    output_final = output_dir / output_file
    with open(output_final, "a") as file:
        file.write(f"{int(price*100):07}{credit_card:16}{description:>16}\n")
