# 11725. 트리의 부모 찾기
# 메모리 kb / 실행시간 ms

import sys

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.friend = set()

def check(node):
    for elem in tree[node].friend:
        if not tree[elem].parent and elem != 1:
            tree[elem].parent = node
            check(elem)


for test_case in range(1, T+1):
    N = int(input())
    tree = {1: Node(1)}
    for _ in range(N-1):
        a, b = map(int, input().split())
        
        if a not in tree:
            tree[a] = Node(a)
        tree[a].friend.add(b)
        if b == 1 and not tree[a].parent:
            tree[a].parent = 1
        
        if b not in tree:
            tree[b] = Node(b)
        tree[b].friend.add(a)
        if a == 1 and not tree[b].parent:
            tree[b].parent = 1
    
    for root_child in tree[1].friend:
        check(root_child)

    for i in range(2, N+1):
        print(tree[i].parent)

        
    














