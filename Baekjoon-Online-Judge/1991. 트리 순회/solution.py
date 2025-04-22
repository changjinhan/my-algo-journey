# 1991. 트리 순회
# 메모리 32,412kb / 실행시간 36ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(node):
    if not node:
        return
    preorder_results.append(node)
    preorder(tree[node].left)
    preorder(tree[node].right)

def inorder(node):
    if not node:
        return
    inorder(tree[node].left)
    inorder_results.append(node)
    inorder(tree[node].right)

def postorder(node):
    if not node:
        return
    postorder(tree[node].left)
    postorder(tree[node].right)
    postorder_results.append(node)
    

for test_case in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N):
        parent, left, right = input().split()
    
        if parent not in tree:
            tree[parent] = Node(parent)
        if left != '.':
            if left not in tree:
                tree[left] = Node(left)
            tree[parent].left = left
        if right != '.':
            if right not in tree:
                tree[right] = Node(right)
            tree[parent].right = right

    # 전위 순회
    preorder_results = []
    preorder('A')
    print(''.join(preorder_results))

    # 중위 순회
    inorder_results = []
    inorder('A')
    print(''.join(inorder_results))

    # 후위 순회
    postorder_results = []
    postorder('A')
    print(''.join(postorder_results))
