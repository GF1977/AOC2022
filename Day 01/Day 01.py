file = open("Day01-Input-p.txt", mode ="r")
snacks = file.read().split("\n")

calories = 0
all_calories = []

for snack in snacks:
    if(snack == ""):
        all_calories.append(calories)
        calories = 0
    else:
        calories = calories + int(snack)

all_calories.append(calories) # The last Elf's snacks
all_calories.sort(reverse=True)

print("Part One = ", all_calories[0])
print("Part two = ", all_calories[0] + all_calories[1] + all_calories[2])

# Answers:
# Part One =  68787
# Part two =  198041