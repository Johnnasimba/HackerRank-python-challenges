from itertools import product


def iter_product(list_a, list_b):
    result = list(product(list_a, list_b, repeat=1))
    for item in result:
        print(item, end=" ")

# Convert the input to string
def list_converter(string):
    numbers_list = [int(a) for a in string.split()]
    return numbers_list


iter_product(list_converter(input()), list_converter(input()))