highest_score = 0
winner_name = ""
scores = []
with open("results.txt") as result_f:
    for line in result_f:
        name, score = line.split()
        scores.append(float(score))
#         if float(score) > highest_score:
#             highest_score = float(score)
#             winner_name = name
# print(f"The highest score was: {highest_score} by {winner_name}")
scores.sort()
scores.reverse()
print("Los tres primeros scores son:")
print(scores[0])
print(scores[1])
print(scores[2])

# Some list methods:
# count()    Returns the number of elements with the specified value
# extend()    Add the elements of a list (or any iterable), to the end of the current list
# index()    Returns the index of the first element with the specified value
# insert()    Adds an element at the specified position
# pop()    Removes the element at the specified position
# remove()    Removes the item with the specified value
# reverse()    Reverses the order of the list
# sort()    Sorts the list
# clear()    Removes all the elements from the list
# copy()    Returns a copy of the list
# list()    Returns a list object
# max()    Returns the largest item in an iterable
# min()    Returns the smallest item in an iterable
# sum()    Returns the sum of all elements in an iterable
# sorted()    Returns a sorted list
