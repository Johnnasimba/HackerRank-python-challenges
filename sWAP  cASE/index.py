# Solution 1
def split(word):
    return [char for char in word]

cased_list = []

def swap_case(s):
    my_list = s.split(" ")
    for item in my_list:
        letters = split(item)
        new_letters = [letter.upper() if letter.islower() else letter.lower() for letter in letters]
        string_letters = "".join(new_letters)
        cased_list.append(string_letters)

    return " ".join(cased_list)



# Solution 2
name = input()
print(''.join(c.lower() if c.isupper() else c.upper() for c in name))


# Solution 3
name = "HackerRank.com presents"
print(name.swapcase())