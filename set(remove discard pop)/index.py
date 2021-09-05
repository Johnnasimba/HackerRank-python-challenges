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


print(sum(s))
