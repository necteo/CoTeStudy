notation = input()
stack = []

def postfix():
    for c in notation:
        if ord('A') <= ord(c) <= ord('Z'):
            stack.append(c)
        elif c == '+' or c == '-' or c == '*' or c == '/':
            stack
        elif c == '(':
            df