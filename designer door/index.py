
n, m = map(int, input().split())
fill_string = '.|.'
middle_string = "WELCOME"

# Upper part

for i in range(n // 2):
    print((fill_string * (i * 2 + 1)).center(m, '-'))

# middle part

print(middle_string.center(m, '-'))

# bottom part
for i in reversed(range(n // 2)):
    print((fill_string * (i * 2 + 1)).center(m, '-'))