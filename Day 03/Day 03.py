file = open("Day03-input-p.txt", mode="r")
rucksacks = file.read().split("\n")

answerPartOne = 0
answerPartTwo = 0

def GetPriority(letter):
    ASCIIcode = ord(letter)
    if (ASCIIcode < 91):  # A-Z  are 65 - 91, all of them are less than 91
        return ASCIIcode - 38  # A = 65
    else:
        return ASCIIcode - 96  # a = 97

def GetCommonItem(A, B):
    result = ""
    for a in A:
        if a in B and a not in result:
            result = result + a
    return result

def GetRucksackGroups(rucksacks):
    groups = []
    for i in range(0,len(rucksacks),3):
        group = [rucksacks[i+0],rucksacks[i+1],rucksacks[i+2]]
        groups.append(group)
    return groups

#Part one
for rucksack in rucksacks:
    compartmentSize = int(len(rucksack) / 2)
    commonItem = GetCommonItem(rucksack[:compartmentSize], rucksack[compartmentSize:])[0]
    answerPartOne = answerPartOne + GetPriority(commonItem[0])

#Part two
groups = GetRucksackGroups(rucksacks)
for group in groups:
    potentialBadge = GetCommonItem(group[0],group[1])
    badge = GetCommonItem(group[2], potentialBadge)
    answerPartTwo = answerPartTwo + GetPriority(badge)

print("----------------------------")
print("Part one:", answerPartOne)
print("Part one:", answerPartTwo)

# Answers:
# Part one: 7674
# Part one: 2805