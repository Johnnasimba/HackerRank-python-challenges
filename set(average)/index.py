def average(array):
    distinct_values = set(array)
    average_height = sum(distinct_values) / len(distinct_values)
    return average_height


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)