import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        try:
            print(self.stack.pop())
        except:
            print(-1)

    def top(self):
        try:
            print(self.stack[-1])
        except:
            print(-1)

    def size(self):
        print(len(self.stack))
    
    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)

cnt = int(sys.stdin.readline())
stk = Stack()

for i in range(cnt):
    cmd = sys.stdin.readline()

    if  cmd[0] == '2':
        stk.pop()
    elif cmd[0] == '5':
        stk.top()
    elif cmd[0] == '3':
        stk.size()
    elif cmd[0] == '4':
        stk.empty()
    else:
        _, a = cmd.split()
        stk.push(a)