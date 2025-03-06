import sys
import collections

input = list(sys.stdin.readline().strip())
new_li = []

for i in input:
    new_li.append(i.lower())

ans = collections.Counter(new_li)

real_ans = [i for i, e in ans.items() if max(ans.values()) == e]

if len(real_ans) == 1:
    print(real_ans[0].upper())
else:
    print('?')