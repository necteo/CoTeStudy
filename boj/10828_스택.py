import sys
input = sys.stdin.readline
stack = []
length = 0
for _ in range(int(input())):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
        length += 1
    elif command[0] == "pop":
        if length > 0:
            print(stack.pop())
            length -= 1
        else:
            print(-1)
    elif command[0] == "top":
        if length > 0:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == "size":
        print(length)
    elif command[0] == "empty":
        print(int(length == 0))