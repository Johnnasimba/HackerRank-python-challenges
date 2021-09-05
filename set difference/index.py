n_english = int(input())
d_english = set(list(map(int, input().split())))

n_french = int(input())
d_french = set(list(map(int, input().split())))

print(len(d_english - d_french))