# 10828. 스택
# 메모리  33,432kb / 실행시간  52ms

import sys

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # N = int(sys.stdin.readline().strip()) # 백준 제출용
    stack = []
    last = None
    size = 0
    for _ in range(N):
        command = input().strip().split()
        # command = sys.stdin.readline().strip().split() # 백준 제출용

        if command[0] == 'push':
            x = int(command[1])
            stack.append(x)
            last = x
            size += 1
        elif command[0] == 'pop':
            if size > 0:
                val = stack.pop()
                size -= 1
                if size > 0:
                    last = stack.pop()
                    stack.append(last)
                print(val)
            else:
                print(-1)
        elif command[0] == 'size':
            print(size)
        elif command[0] == 'empty':
            if size == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'top':
            if size > 0:
                print(last)
            else:
                print(-1)
            














