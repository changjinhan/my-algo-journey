# 18258. 큐 2
# 메모리  144,372kb / 실행시간  1,896ms

import sys
from collections import deque

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

class Queue:
    def __init__(self):
        self.queue = deque([])
        self.first = None
        self.last = None
        self.len = 0
    
    def push(self, x):
        self.queue.append(x)
        if self.len == 0:
            self.first = x
        self.last = x
        self.len += 1
    
    def pop(self):
        if self.len > 0:
            val = self.queue.popleft()
            self.len -= 1
            if self.len == 0:
                self.first = None
                self.last = None
            else:
                self.first = self.queue.popleft()
                self.queue.appendleft(self.first)
            return val
        else:
            return -1
        
    def size(self):
        return self.len
    
    def empty(self):
        return 1 if self.len == 0 else 0
    
    def front(self):   
        return self.first if self.first else -1
    
    def back(self):
        return self.last if self.last else -1


for test_case in range(1, T+1):
    N = int(input())
    # N = int(sys.stdin.readline().strip()) # 백준 사이트 제출용
    queue = Queue()

    for _ in range(N):
        command = input()
        # command = sys.stdin.readline().strip() # 백준 사이트 제출용
        if len(command.split()) == 2: # push
            x = int(command.split()[1])
            queue.push(x)
        elif command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.size())
        elif command == 'empty':
            print(queue.empty())
        elif command == 'front':
            print(queue.front())
        elif command == 'back':
            print(queue.back())













