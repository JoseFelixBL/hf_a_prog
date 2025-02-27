highest_score = 0
winner_name = ""
scores = {}
with open("results.txt") as result_f:
    for line in result_f:
        name, score = line.split()
        scores[name] = float(score)

for name, score in scores.items():
    print(f"{name}\t{score}")
