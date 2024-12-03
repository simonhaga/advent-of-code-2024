lefts = []
rights = []

for line in open('input.txt').readlines():
    lefts.append(int(line[0:5]))
    rights.append(int(line[8:]))

lefts.sort()
rights.sort()

distance = 0

for i, item in enumerate(lefts):
    left = lefts[i]
    right = rights[i]
    distance += abs(left - right)

print(distance)
