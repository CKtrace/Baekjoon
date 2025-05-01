import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    cards = sys.stdin.readline().split()
    dq = deque()
    dq.append(cards[0])
    for cr in cards[1:]:
        if cr <= dq[0]:
            dq.appendleft(cr)
        else:
            dq.append(cr)

    print(''.join(dq))