lefts = []
rights = []

for line in open('input.txt').readlines():
    lefts.append(int(line[0:5]))
    rights.append(int(line[8:]))

similarity_score = 0

for left in lefts:
    for right in rights:
        if right == left:
            similarity_score += left

print(similarity_score)
