# 11725. 트리의 부모 찾기
# DFS 풀이: RecursionError
# BFS 풀이: 메모리 79,568kb / 실행시간 628ms


import sys
from collections import deque

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.friend = set()

def dfs(node):    
    for elem in tree[node].friend:
        if not tree[elem].parent:
            tree[elem].parent = node
            dfs(elem)

def bfs(node):
    q = deque([node])

    while q:
        cur = q.popleft()
        for elem in tree[cur].friend:
            if not tree[elem].parent:
                tree[elem].parent = cur
                q.append(elem)
    

for test_case in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N-1):
        a, b = map(int, input().split())
        
        if a not in tree:
            tree[a] = Node(a)
        if b not in tree:
            tree[b] = Node(b)

        tree[a].friend.add(b)
        tree[b].friend.add(a)
    
    tree[1].parent = -1
    # dfs(1)
    bfs(1)

    for i in range(2, N+1):
        print(tree[i].parent)

        
