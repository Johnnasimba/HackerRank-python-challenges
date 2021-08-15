def print_formatted(n):    
    space_padding = len(bin(n)[2:])

    for i in range(1, n + 1):
        print(
            str(i).rjust(space_padding),
            str(oct(i)[2:]).rjust(space_padding),
            str(hex(i)[2:].upper()).rjust(space_padding),
            str(bin(i)[2:]).rjust(space_padding),
        )
