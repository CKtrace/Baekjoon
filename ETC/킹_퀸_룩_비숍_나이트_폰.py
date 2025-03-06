import sys

input = list(map(int, sys.stdin.readline().split()))
new_li = []
cnt = 0
for i in input:
    if cnt == 0 or cnt == 1:
        new_li.append(1 - i)
        cnt += 1
    elif cnt == 2 or cnt == 3 or cnt == 4:
        new_li.append(2 - i)
        cnt += 1
    elif cnt == 5:
        new_li.append(8 - i)
        break 

print(*new_li)   