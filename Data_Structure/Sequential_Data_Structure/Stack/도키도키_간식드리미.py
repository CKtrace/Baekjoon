import sys

front_stu = int(input())
order = list(map(int, sys.stdin.readline().split()))
save_order = order.copy()
sub_stack = []
cnt = 1


for i in save_order:
    if i == cnt:
        del order[0]
        cnt += 1
    else:
        sub_stack.append(i)
        del order[0]
    if len(sub_stack) != 0:
        for a in list(reversed(sub_stack)):
            if a == cnt:
                del sub_stack[-1]
                cnt += 1
            else:
                break


if len(sub_stack) != 0:
    print('Sad')
else:
    print('Nice')

