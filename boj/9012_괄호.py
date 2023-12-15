for _ in range(int(input())):
    s = input()
    check = []
    ans = "YES"
    for i in s:
        c = 0
        if i == "(" or i == "[":
            check.append(i)
        elif i == ")":
            if check:
                c = check.pop()
            if c != "(":
                ans = "NO"
                break
        elif i == "]":
            if check:
                c = check.pop()
            if c != "[":
                ans = "NO"
                break
    if check:
        ans = "NO"
    print(ans)