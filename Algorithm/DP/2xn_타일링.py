N = int(input())
dp_li = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp_li[i] = 1
    if i == 2:
        dp_li[i] = 2
    if i >= 3:
        dp_li[i] = dp_li[i-1] + dp_li[i-2]

print(dp_li[N] % 10007)