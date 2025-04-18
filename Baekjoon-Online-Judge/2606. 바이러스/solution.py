# 2606. 바이러스
# DFS: 메모리  32,412kb / 실행시간  36ms
# BFS: 메모리  34,924kb / 실행시간  56ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

# DFS 풀이
def dfs(cur):
    if sum(connected[cur]) == 0:
        return

    for nxt in range(num_com):
        if connected[cur][nxt] == 1 and not virus_coms[nxt]:
            virus_coms[nxt] = True
            dfs(nxt)

# BFS 풀이
from collections import deque

def bfs(start):
    queue = deque([start])
    virus_coms[start] = True

    while queue:
        cur = queue.popleft()
        for nxt in range(num_com):
            if connected[cur][nxt] == 1 and not virus_coms[nxt]:
                virus_coms[nxt] = True
                queue.append(nxt)


for test_case in range(1, T+1):
    num_com = int(input())
    num_pair = int(input())
    
    connected = [[0] * num_com for _ in range(num_com)]
    connected[0][0] = 1
    for _ in range(num_pair):
        x, y = map(int, input().split())
        connected[x-1][y-1] = 1
        connected[y-1][x-1] = 1

    virus_coms = [False] * num_com
    dfs(0)
    # bfs(0)

    print(sum(virus_coms)-1)










