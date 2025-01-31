import sys

class QUEUE:
    def __init__(self):
        self.que = []

    def push(self, x):
        self.que.append(x)

    def pop(self):
        if len(self.que) == 0:
            print(-1)
        else:
            pop_ele = self.que[0]
            del self.que[0]
            print(pop_ele) 

    def size(self):
        print(len(self.que))
    
    def empty(self):
        if len(self.que) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.que) == 0:
            print(-1)
        else:
            print(self.que[0])

    def back(self):
        if len(self.que) == 0:
            print(-1)
        else:
            print(self.que[-1])


N = int(input())
que = QUEUE()
cmd = []

for i in range(N):
    cmd = sys.stdin.readline().split()
    
    if len(cmd) > 1:
        que.push(cmd[1])
    
    else:
        if cmd[0] == 'pop':
            que.pop()
        elif cmd[0] == 'size':
            que.size()
        elif cmd[0] == 'empty':
            que.empty()
        elif cmd[0] == 'front':
            que.front()
        elif cmd[0] == 'back':
            que.back()
