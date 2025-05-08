# 16236. 아기 상어
# 메모리 35,036kb / 실행시간 96ms

import sys
from collections import deque
sys.stdin = open('./sample_input.txt', 'r')

def bfs(shark_pos, shark_size):
    visited = [[False] * N for _ in range(N)]
    dist = 0
    q = deque()
    q.append((shark_pos, dist))
    visited[shark_pos[0]][shark_pos[1]] = True
    candidates = []
    while q:
        (x, y), dist = q.popleft()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if sea_space[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0 < sea_space[nx][ny] < shark_size:
                        candidates.append((dist + 1, nx, ny))
                    else:
                        q.append(((nx, ny), dist + 1))
    if not candidates:
        return None, float('inf')
    candidates.sort()
    d, fx, fy = candidates[0]
    return (fx, fy), d

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sea_space = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if sea_space[r][c] == 9:
                shark_pos = (r, c)
                break
    time = 0
    shark_size = 2
    count = 0
    while True:
        next_fish, d = bfs(shark_pos, shark_size)
        if not next_fish:
            print(time)
            break
        sea_space[shark_pos[0]][shark_pos[1]] = 0
        sea_space[next_fish[0]][next_fish[1]] = 0
        shark_pos = next_fish
        count += 1
        if count == shark_size:
            shark_size += 1
            count = 0
        time += d

            

    









