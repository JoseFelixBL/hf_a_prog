highest_score = 0
result_f = open("results.txt")
for line in result_f:
    if float(line) > highest_score:
        highest_score = float(line)
result_f.close()
print(f"The highest score was: {highest_score}")
