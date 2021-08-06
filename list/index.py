if __name__ == '__main__':
    N = int(input())
    
my_list = []
for n in range(N):
    user_input = input().split(" ")
    if len(user_input) == 3:
        my_list.insert(int(user_input[1]), int(user_input[2]))
    elif len(user_input) == 2:
        if user_input[0] == 'remove':
            my_list.remove(int(user_input[1]))
        elif user_input[0] == 'append':
            my_list.append(int(user_input[1]))
    else:
        if user_input[0] == 'print':
            print(my_list)
        elif user_input[0] == 'sort':
            my_list = sorted(my_list, reverse=False)
        elif user_input[0] == 'pop':
            my_list.pop()
        elif user_input[0] == 'reverse':
            my_list.reverse()
    