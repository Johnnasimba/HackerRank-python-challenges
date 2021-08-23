from itertools import permutations
string = input()
# convert string into list
my_list = [item for item in string.split(' ')]
# Extract the values from the list
s = my_list[0]
r = int(my_list[1])

result = list(permutations(sorted(s), r))

for item in result:
    print(''.join(item))