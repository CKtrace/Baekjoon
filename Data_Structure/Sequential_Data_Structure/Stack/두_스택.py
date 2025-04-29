import sys

N, K = map(int, sys.stdin.readline().split())
bag_1 = list(map(int, sys.stdin.readline().split()))
bag_2 = list(map(int, sys.stdin.readline().split()))

total_A = sum(bag_1)
total_B = sum(bag_2)

min_heavy_bag = float('inf')

prefix_sum_A = [0] * (N + 1)
prefix_sum_B = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum_A[i] = prefix_sum_A[i - 1] + bag_1[-i]
    prefix_sum_B[i] = prefix_sum_B[i - 1] + bag_2[-i]

for i in range(0, min(N, K) + 1):
    j = K - i
    if j > N:
        continue

    remain_A = total_A - prefix_sum_A[i]
    remain_B = total_B - prefix_sum_B[j]

    heavier = max(remain_A, remain_B)

    min_heavy_bag = min(heavier, min_heavy_bag)

print(min_heavy_bag)