s = input()
while s != ".":
    check = []
    ans = "yes"
    for i in s:
        c = 0
        if i == "(" or i == "[":
            check.append(i)
        elif i == ")":
            if check:
                c = check.pop()
            if c != "(":
                ans = "no"
                break
        elif i == "]":
            if check:
                c = check.pop()
            if c != "[":
                ans = "no"
                break
    if check:
        ans = "no"
    print(ans)
    s = input()