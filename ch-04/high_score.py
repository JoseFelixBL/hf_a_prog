highest_score = 0
winner_name = ""
scores = {}
with open("results.txt") as result_f:
    for line in result_f:
        name, score = line.split()
        scores[score] = name

# for name, score in scores.items():
#     print(f"{score}\t{name}")

for ord_score in sorted(scores.keys(), reverse=True):
    print(f"{ord_score}\t{scores[ord_score]}")
