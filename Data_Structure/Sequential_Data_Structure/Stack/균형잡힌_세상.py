import sys

while True:
    txt = list(sys.stdin.readline())
    ans = []
    if txt[0] == '.':
        break

    for i in range(len(txt)):
        if txt[i] == '(' or txt[i] == ')' or txt[i] == '[' or txt[i] == ']':
            ans += (txt[i])
            if ans[0] == ')' or ans[0] == ']':
                pass
            elif (ans[-1] == ')' and ans[-2] == '(') or (ans[-1] == ']' and ans[-2] == '['):
                ans.pop(-2)
                ans.pop(-1)
        
    if not ans:
        print("yes")
    else:
        print("no")

    txt, ans = [], []