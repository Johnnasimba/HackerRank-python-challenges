def print_rangoli(size):
    n = size
    # generate list of letters
    li = list(map(chr, range(97, 123)))
    # reverse list
    x = li[n-1::-1] + li[1:n]
    # padding space
    space_padding = len('-'.join(x))

    # upper part
    for i in range(1, n):
        print('-'.join(li[n-1:n-i:-1] + li[n-i:n]).center(space_padding, '-'))
    # bottom part
    for i in range(n, 0, -1):
        print('-'.join(li[n-1:n-i:-1] + li[n-i:n]).center(space_padding, '-'))
