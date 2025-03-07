import sys

X = []
Y = []

a, b = map(int, sys.stdin.readline().split(' '))

for i in range(a):
    i = list(map(int, input().split()))
    X.append(i)

for i in range(a):
    i = list(map(int, input().split()))
    Y.append(i)

for p in range(a):
    for q in range(b):
        print(X[p][q] + Y[p][q], end=' ')
    print()
