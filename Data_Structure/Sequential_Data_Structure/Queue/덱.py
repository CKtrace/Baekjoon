import sys

class Dequeue:
    def __init__(self):
        self.item = []

    def push_front(self, x):
        self.item.insert(0, x)

    def push_back(self, x):
        self.item.append(x)

    def pop_front(self):
        if len(self.item) != 0:
            print(self.item.pop(0))
        else:
            print(-1)

    def pop_back(self):
        if len(self.item) != 0:
            print(self.item.pop())
        else:
                print(-1)

    def size(self):
        print(len(self.item))

    def empty(self):
        if len(self.item) != 0:
            print(0)
        else:
            print(1)

    def front(self):
        if len(self.item) == 0:
            print(-1)
        else:
            print(self.item[0])

    def back(self):
        if len(self.item) == 0:
            print(-1)
        else:
            print(self.item[-1])


D = Dequeue()

N = int(sys.stdin.readline())
command_list = []

for i in range(N):
    cmd = list(sys.stdin.readline().split())
    command_list.append(cmd)

for i in command_list:
    if len(i) == 1:
        if i[0] == 'front':
            D.front()
        elif i[0] == 'back':
            D.back()
        elif i[0] == 'size':
            D.size()
        elif i[0] == 'empty':
            D.empty()
        elif i[0] == 'pop_front':
            D.pop_front()
        elif i[0] == 'pop_back':
            D.pop_back()
    else:
        if i[0] == 'push_front':
            D.push_front(int(i[1]))
        else:
            D.push_back(int(i[1]))