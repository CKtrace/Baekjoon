class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            return -1

    def top(self):
        try:
            return self.stack[-1]
        except:
            return -1

    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0


cnt = int(input())
cmd_list = []
stk = Stack()

for i in range(cnt):
    cmd = input()
    cmd_list.append(cmd)


for i in cmd_list:
    if i == 'pop':
        print(stk.pop())
    elif i == 'top':
        print(stk.top())
    elif i == 'size':
        print(stk.size())
    elif i == 'empty':
        print(stk.empty())
    else:
        _, a = i.split()
        stk.push(a)