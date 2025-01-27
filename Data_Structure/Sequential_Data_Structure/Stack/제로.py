a = int(input())
stack = []

for i in range(a):
    cmd = int(input())
    if cmd == 0:
        stack.pop()
    else:
        stack.append(cmd)

ans = 0

if len(stack) != 0:
    for i in stack:
        ans += int(i)
    print(ans)
else:
    print(0)