import sys 

A = []

for i in range(5):
    a = list(map(str, sys.stdin.readline().strip()))
    A.append(a)

ans = ''

len_li = [len(A[0]), len(A[1]), len(A[2]), len(A[3]), len(A[4])]
len_len = max(len_li)

for a in range(len_len):
    if a < len(A[0]):
        ans += A[0][a]
    if a < len(A[1]):
        ans += A[1][a]
    if a < len(A[2]):
        ans += A[2][a]    
    if a < len(A[3]):
        ans += A[3][a]
    if a < len(A[4]):
        ans += A[4][a]
print(ans)