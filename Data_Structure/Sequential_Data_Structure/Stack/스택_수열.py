import sys

N = int(input())
condition = True
cnt = 1
stack = []
oper = []

for i in range(N):
    maker = int(sys.stdin.readline())

    while cnt <= maker:
        stack.append(cnt)
        oper.append('+')
        cnt += 1

    if stack[-1] == maker:
        stack.pop()
        oper.append('-')

    else:
        condition = False
        break

if condition == False:
    print('NO')
else:
    for op in oper:
        print(op)