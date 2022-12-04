file = open("Day04-input-p.txt", mode="r")
sections = file.read().split("\n")
def GetOverlappingType(sectionAtxt, sectionBtxt):
    # return OverlappingTypes
    # 0 - no overlapping
    # 1 - one section is fully within other
    # 2 - partial overlapping
    sA = [int(sectionAtxt[0]), int(sectionAtxt[1])]
    sB = [int(sectionBtxt[0]), int(sectionBtxt[1])]

    if (sA[0] >= sB[0] and sA[1] <= sB[1]) or (sB[0] >= sA[0] and sB[1] <= sA[1]):
        return 1

    # there are only two cases of partial overlapping
    # 1.
    #      ******
    #           **************
    # 2.
    #               ****************
    #            *********
    if (sA[0] < sB[0] and sA[1] >= sB[0]) or (sB[0] < sA[0] and sB[1] >= sA[0]):
        return 2

    return 0

fullyOverlapped     = 0
partiallyOverlapped = 0
for section in sections:
    pair = section.split(",")
    OverlappingType = GetOverlappingType(pair[0].split("-"), pair[1].split("-"))
    if OverlappingType == 1 :
        fullyOverlapped = fullyOverlapped + 1
    if OverlappingType == 2:
        partiallyOverlapped = partiallyOverlapped + 1

print("----------------------------")
print("Part One:", fullyOverlapped)
print("Part Two:", fullyOverlapped + partiallyOverlapped)

# Answers:
# Part one: 494
# Part one: 833