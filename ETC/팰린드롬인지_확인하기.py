import sys

input = list(sys.stdin.readline().strip())

if list(reversed(input)) == input:
    print(1)

else:
    print(0)