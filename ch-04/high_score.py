highest_score = 0
winner_name = ""
with open("results.txt") as result_f:
    for line in result_f:
        name, score = line.split()
        if float(score) > highest_score:
            highest_score = float(score)
            winner_name = name
# result_f.close()
print(f"The highest score was: {highest_score} by {winner_name}")
