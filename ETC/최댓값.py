A = []
max_A = []

for i in range(9):
    i = list(map(int, input().split()))
    A.append(i)

for i in range(9):
    max_A.append(max(A[i]))

p = max_A.index(max(max_A))
print(max(max_A))
print(p + 1 , A[p].index(max(A[p])) + 1)