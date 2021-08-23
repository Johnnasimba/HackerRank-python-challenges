import numpy

n, m = map(int, input().split())
my_list = []
for i in range(n):
    n, m = map(int, input().split())
    my_list.append([n, m])


my_array = numpy.array(my_list)

min_value = numpy.min(my_array, axis=1)
max_value = numpy.max(min_value)
print(max_value)
