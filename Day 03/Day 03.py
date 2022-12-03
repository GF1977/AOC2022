file = open("Day03-input-p.txt", mode="r")
rucksacks = file.read().split("\n")

answerPartOne = 0
answerPartTwo = 0


def GetPriority(letter):
    ASCIIcode = ord(letter)
    if (ASCIIcode < 91):  # A-Z  are 65 - 91, all of them are less then 91
        return ASCIIcode - 38  # A = 65
    else:
        return ASCIIcode - 96  # a = 97


def GetCommonItem(A, B):
    result = []
    for a in A:
        for b in B:
            if a == b:
                result.append(a)
    return result

for rucksack in rucksacks:
    compartmentSize = int(len(rucksack) / 2)
    # print(compartmentSize)
    leftC = rucksack[:compartmentSize]
    rightC = rucksack[compartmentSize:]
    # print(leftC,":",rightC)
    commonItem = GetCommonItem(leftC, rightC)[0]
    answerPartOne = answerPartOne + GetPriority(commonItem)
    # print(commonItem, " = ", GetPriority(commonItem))

print("----------------------------")
print("Part one:", answerPartOne)
print("Part one:", answerPartTwo)

# Answers:
# Part one: 7674
# Part one:
