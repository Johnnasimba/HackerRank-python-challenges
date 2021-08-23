from itertools import combinations_with_replacement

s, r = input().split(' ')
r = int(r)

for item in list(combinations_with_replacement(sorted(s), r)):
    print(''.join(item))