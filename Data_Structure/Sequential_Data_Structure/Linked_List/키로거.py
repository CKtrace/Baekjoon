import sys

class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self
    
    def __str__(self):
        return str(self.key)
    

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    
    def __str__(self):
        return "".join(str(v.key) for v in self)
    
    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        a.prev.next = b.next
        b.next.prev = a.prev

        x.next.prev = b
        b.next = x.next
        x.next = a
        a.prev = x

    def moveAfter(self, a, x):
        self.splice(a, a, x)
    
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
    
    def removeNode(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev

N = int(input())
cmd = []

for i in range(N):
    cmd.append(list(sys.stdin.readline().strip()))

for li in cmd:
    LL = DoublyLinkedList()
    cur = Node('|')
    cur.next = LL.head
    cur.prev = LL.head

    LL.head.next = cur
    LL.head.prev = cur
    for ele in li:
        if ele == '<':
            if cur.prev.key == None:
                continue
            else:
                LL.moveBefore(cur, cur.prev)
        elif ele == '>':
            if cur.next.key == None:
                continue
            else:
                LL.moveAfter(cur, cur.next)
        elif ele == '-':
            if cur.prev.key == None:
                continue
            else:
                LL.removeNode(cur.prev)
        else:
            LL.insertBefore(cur, ele)

    LL.removeNode(cur)
    print(LL)
