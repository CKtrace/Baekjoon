import sys
from collections import deque

N = int(sys.stdin.readline())
ans = deque()
cmd = []

for i in range(N):
    cmd.append(list(sys.stdin.readline().split()))

for i in cmd:
    if len(i) != 1:
        ans.append(int(i[-1]))
    else:
        if i[0] == 'pop':
            if len(ans) != 0:
                print(ans[0])
                ans.popleft()
            else:
                print(-1)
        elif i[0] == 'size':
            print(len(ans))
        elif i[0] == 'empty':
            if len(ans) == 0:
                print(1)
            else:
                print(0)
        elif i[0] == 'front':
            if len(ans) != 0:
                print(ans[0])
            else:
                print(-1)
        elif i[0] == 'back':
            if len(ans) != 0:
                print(ans[-1])
            else:
                print(-1)