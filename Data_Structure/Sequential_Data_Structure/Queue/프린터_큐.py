from collections import deque
import sys

N = int(input())

for i in range(N):
    doc_feature = list(map(int, sys.stdin.readline().split()))
    doc = deque(map(int, sys.stdin.readline().split()))
    idx = deque(range(0, doc_feature[0]))
    cnt = 0

    while True:
        if doc[0] == max(doc):
            cnt += 1

            if idx[0] == doc_feature[1]:
                print(cnt)
                break
            else:
                doc.popleft()
                idx.popleft()

        else:
            doc.append(doc.popleft())
            idx.append(idx.popleft())
