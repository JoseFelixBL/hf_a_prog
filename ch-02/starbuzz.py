from io import open
import time
from random import randrange


# print(text[247:251])
start_of_price = 247
end_of_price = 251
price = 99.99
while price > 4.74:
    time.sleep(1)
    with open("beansrus.html", "r") as page:
        text = page.read()
    price = float(text[start_of_price:end_of_price])
    price += randrange(-15, 15)/10
    print(f'{"."*5} {price}')
print(f"Buy at {price}")


""" Other built-in string methods
text.endswith(".jpg") # Returns True if the string ends with ".jpg"
text.startswith("http") # Returns True if the string starts with "http"
text.upper() # Converts all characters to uppercase
text.lower() # Converts all characters to lowercase
text.replace("tomorrow", "Tuesday") # Replaces all occurrences of "tomorrow" with "Tuesday"
text.strip()  # Removes leading and trailing whitespace
text.split()  # Splits the string into a list of strings
text.splitlines()  # Splits the string into a list of strings at line breaks
text.join(["http://", ".com"])  # Joins the elements of a list into a single string
text.find("python")  # Returns the index of the first occurrence of "python" in the string
text.rfind("python")  # Returns the index of the last occurrence of "python" in the string
text.index("python")  # Returns the index of the first occurrence of "python" in the string
text.rindex("python")  # Returns the index of the last occurrence of "python" in the string
text.count("python")  # Returns the number of occurrences of "python" in the string
text.isalnum()  # Returns True if the string is alphanumeric
text.isalpha()  # Returns True if the string is alphabetic
text.isdigit()  # Returns True if the string is numeric
text.isspace()  # Returns True if the string is whitespace
text.istitle()  # Returns True if the string is titlecased
text.islower()  # Returns True if the string is lowercase
text.isupper()  # Returns True if the string is uppercase
text.isnumeric()  # Returns True if the string is numeric
text.isdecimal()  # Returns True if the string is decimal
text.isidentifier()  # Returns True if the string is a valid identifier
text.isprintable()  # Returns True if the string is printable
text.isascii()  # Returns True if the string is ASCII
"""
