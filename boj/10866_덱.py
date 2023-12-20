import sys
input = sys.stdin.readline
MAX_SIZE = 10001
queue = [0 for i in range(MAX_SIZE)]
front = 0
rear = 0
for _ in range(int(input())):
    command = input().split()
    if command[0] == "push_front":
        queue[front] = int(command[1])
        front = (front-1+MAX_SIZE) % MAX_SIZE
    elif command[0] == "push_back":
        rear = (rear+1) % MAX_SIZE
        queue[rear] = int(command[1])
    elif command[0] == "pop_front":
        if front != rear:
            front = (front+1) % MAX_SIZE
            print(queue[front])
        else:
            print(-1)
    elif command[0] == "pop_back":
        if front != rear:
            print(queue[rear])
            rear = (rear-1+MAX_SIZE) % MAX_SIZE
        else:
            print(-1)
    elif command[0] == "size":
        if front <= rear:
            print(rear-front)
        else:
            print(rear+MAX_SIZE-front)
    elif command[0] == "empty":
        print(int(front == rear))
    elif command[0] == "front":
        if front != rear:
            print(queue[(front+1) % MAX_SIZE])
        else:
            print(-1)
    elif command[0] == "back":
        if front != rear:
            print(queue[rear])
        else:
            print(-1)