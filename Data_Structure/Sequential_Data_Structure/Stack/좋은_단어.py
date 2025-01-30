import sys

N = int(input())
word = []
stack = []
ans = 0

for i in range(N):
    voca = list(sys.stdin.readline())
    voca.pop()
    word.append(voca)

for a in word:
    for b in a:
        if len(stack) != 0 and b == stack[-1]:
            stack.pop()
        else:
            stack.append(b)
    if len(stack) == 0:
        ans += 1
    stack = []

print(ans)