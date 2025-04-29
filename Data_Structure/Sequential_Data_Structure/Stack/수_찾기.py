import sys

a = int(sys.stdin.readline())
li_a = set(map(int, sys.stdin.readline().split()))

b = int(sys.stdin.readline())
li_b = list(map(int, sys.stdin.readline().split()))

for p in li_b:
    if p in li_a:
        print(1)
    else:
        print(0)
