from collections import deque
import sys

N, M = list(map(int, sys.stdin.readline().split()))
idx = list(map(int, sys.stdin.readline().split()))

N_deque = deque([i for i in range(1, N+1)])

count = 0

for i in idx:
    while True:
        if N_deque[0] == i:
            N_deque.popleft()
            break
        else:
            if N_deque.index(i) > (len(N_deque)//2):
                while N_deque[0] != i:
                    N_deque.rotate(1)
                    count += 1
            else:
                while N_deque[0] != i:
                    N_deque.rotate(-1)
                    count += 1

print(count)