file = open("Day02-Input-p.txt", mode = "r")
gamePlan = file.read().split("\n")

# A for Rock, B for Paper, and C for Scissors
# Scores: (1 for Rock, 2 for Paper, and 3 for Scissors)
# Scores: (0 if you lost, 3 if the round was a draw, and 6 if you won)

myCodes = {"X": "A", "Y": "B", "Z": "C"}

# first letter from my opponent, second - from me
# n + m  means: n = bonus for lost, draw, won    m =  bonus for rock, paper, scissors
results = {"AA": 3 + 1, "AB": 6 + 2, "AC": 0 + 3,"BA": 0 + 1,"BB": 3 + 2, "BC": 6 + 3, "CA": 6 + 1, "CB": 0 + 2, "CC": 3 + 3}

def Game(scenario):
    return results[scenario]

totalScore = 0
for round in gamePlan:
    scenario = round[0] + myCodes[round[2]]
    res = Game(scenario)
    totalScore = totalScore + res

print("----------------------------------")
print("Part one:", totalScore)







