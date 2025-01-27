import sys

n = int(sys.stdin.readline())
li_n = list(map(int, sys.stdin.readline().split()))
stack = []
res = [-1] * n

for i in range(n):
    while stack and li_n[stack[-1]] < li_n[i]:
        res[stack.pop()] = li_n[i]
    stack.append(i)

for num in res:
    print(num, end=' ')