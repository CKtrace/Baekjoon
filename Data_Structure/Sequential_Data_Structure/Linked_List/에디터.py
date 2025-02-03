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


LL = DoublyLinkedList()
cur = Node('|')
cur.next = LL.head
cur.prev = LL.head

LL.head.next = cur
LL.head.prev = cur

text = list(sys.stdin.readline().strip())
for i in text:
    LL.insertBefore(cur, i)

N = int(sys.stdin.readline().strip())
for i in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[0] == 'L' and cur.prev.key != None:
        LL.moveBefore(cur, cur.prev)
    elif cmd[0] == 'D' and cur.next.key != None:
        LL.moveAfter(cur, cur.next)
    elif cmd[0] == 'B' and cur.prev.key != None:
        LL.removeNode(cur.prev)
    elif cmd[0] == 'P':
        LL.insertBefore(cur, cmd[2])

LL.removeNode(cur)
print(LL)