import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

N_deque = deque([i for i in range(1, N+1)])
N_store = []
cnt = 1


while N_deque:
    if cnt % K == 0:
        cnt += 1
        N_store.append(N_deque.popleft())
        if len(N_deque) == 0:
            break

    else:
        cnt += 1
        x = N_deque[0]
        N_deque.popleft()
        N_deque.append(x)



print(str(N_store).replace('[', '<').replace(']', '>'))