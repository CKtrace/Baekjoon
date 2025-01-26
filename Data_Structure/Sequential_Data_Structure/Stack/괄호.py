cnt = int(input())
li = [0] * cnt

for i in range(cnt):
    li[i] = input()

for a in li:
    ck_list = []
    for i in a:
        if i == "(":
            ck_list.append(i)
        elif i == ")" and len(ck_list) != 0:
            if i != ck_list[-1]:
                ck_list.pop()
            elif i == ck_list[-1]:
                ck_list.append(i)
        elif i == ")" and len(ck_list) == 0:
                ck_list.append(i)
    if len(ck_list) == 0:
        print("YES")
    else:
        print("NO")