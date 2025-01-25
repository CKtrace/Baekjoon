a1, a2 = input().split()
a1 = int(a1)
a2 = int(a2)
c = int(input())
n0 = int(input())

if ((a1*n0)+a2) <= (c*n0) and  a1 <= c:
    print(1)
else:
    print(0)