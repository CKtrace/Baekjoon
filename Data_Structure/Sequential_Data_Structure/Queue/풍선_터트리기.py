import sys
from collections import deque

N = int(input())
order_li = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while order_li:
    idx, ord = order_li.popleft()
    ans.append(idx + 1)

    if ord > 0:
        order_li.rotate(-(ord-1))
    elif ord < 0:
        order_li.rotate(-ord)

print(*ans)