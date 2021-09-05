n = int(input())
s = set(map(int, input().split()))
m = int(input())


for i in range(m):
    command_list = list(input().split())
    command = command_list[0]
    if command == "pop":
        s.pop()
    elif command == "remove":
        element = int(command_list[1])
        s.remove(element)
    elif command == "discard":
        element = int(command_list[1])
        s.discard(element)

sum_of_elements = 0

for i in s:
    sum_of_elements = sum_of_elements + i

print(sum_of_elements)