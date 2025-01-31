import sys

N = int(sys.stdin.readline())
score = []

for i in range(N):
    score_ele = float(sys.stdin.readline())
    score.append(score_ele)

for a in (sorted(score))[:7]:
    print(f"{a:.3f}")