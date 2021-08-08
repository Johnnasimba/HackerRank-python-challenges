# Solution 1
if __name__ == '__main__':
    S = input()  

def validator(arr):
    if len(arr) > 0:
        print("True")
    else:
        print("False")


alphanum = [i for i in S if i.isalnum()]
validator(alphanum)

alphabet = [i for i in S if i.isalpha()]
validator(alphabet)

digits = [i for i in S if i.isdigit()]
validator(digits)

lower_letters = [i for i in S if i.islower()]
validator(lower_letters)

upper_letters = [i for i in S if i.isupper()]
validator(upper_letters)


# Solution 2

S = input()

print(any(x.isalnum() for x in S))
print(any(x.isalpha() for x in S))
print(any(x.isdigit() for x in S))
print(any(x.islower() for x in S))
print(any(x.isupper() for x in S))