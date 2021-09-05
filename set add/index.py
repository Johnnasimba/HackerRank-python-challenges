n = int(input())
list_of_stamps = []

for i in range(n):
    list_of_stamps.append(input())
    

distinct_stamps = set(list_of_stamps)
num_distinct_stamps = len(distinct_stamps)

print(num_distinct_stamps)