from collections import deque

N = int(input())
ans_deque = deque([i for i in range(1, N+1)])

while(len(ans_deque)>1):
    ans_deque.popleft()
    move_num = ans_deque.popleft()
    ans_deque.append(move_num)

print(ans_deque[0])