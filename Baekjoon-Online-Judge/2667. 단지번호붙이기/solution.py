# 2667. 단지번호붙이기
# DFS: 메모리  34,968kb / 실행시간  56ms
# BFS: 메모리  34,968kb / 실행시간  56ms

import sys

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

# DFS 풀이
# from collections import Counter
# def dfs(start, group):
#     x, y = start
#     for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if house_map[nx][ny] == 1 and group_map[nx][ny] == 0:
#                 group_map[nx][ny] = group
#                 dfs((nx, ny), group)

# for test_case in range(1, T+1):
#     N = int(input())
#     house_map = [list(map(int, input().strip())) for _ in range(N)]
#     group_map = [[0] * N for _ in range(N)]
    
#     group = 0
#     for x in range(N):
#         for y in range(N):
#             if house_map[x][y] == 1 and group_map[x][y] == 0:
#                 group += 1
#                 group_map[x][y] = group
#                 dfs((x, y), group)
#     print(group) # 총 단지수
    
#     flat_list = []
#     for line in group_map:
#         flat_list.extend(line)
#     counter = Counter(flat_list).most_common()
#     rev_counter = sorted(counter, key=lambda x: x[1])
#     for k, v in rev_counter:
#         if k != 0:
#             print(v) # 단지내 집의 수


# BFS 풀이
from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if house_map[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    return count


for test_case in range(1, T+1):
    N = int(input())
    house_map = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    sizes = []
    for x in range(N):
        for y in range(N):
            if house_map[x][y] == 1 and not visited[x][y]:
                sizes.append(bfs((x, y)))

    print(len(sizes)) # 총 단지 수
    for size in sorted(sizes): 
        print(size) # 단지내 집의 수








