from itertools import combinations

# Extract the values
s, r = input().split(' ')
r = int(r)


for num in range(1, r + 1):
    for item in [item for item in combinations(sorted(s), num)]:
        print(''.join(item))
        