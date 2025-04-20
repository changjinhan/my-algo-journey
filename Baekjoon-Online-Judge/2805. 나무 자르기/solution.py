# 2805. 나무 자르기
# 메모리 148,224kb / 실행시간 3,464ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

def cut_sum(m):
    cut_heights = map(lambda x: x - m if x > m else 0, tree_heights)
    return sum(cut_heights)


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    tree_heights = list(map(int, input().split()))
    tree_heights = sorted(tree_heights)
    max_height = tree_heights[-1]
    
    l, r = 0, max_height-1
    while l <= r:
        m = (l + r) // 2
        if cut_sum(m) >= M:
            l = m + 1
        else:
            r = m - 1

    print(min(l, r))





