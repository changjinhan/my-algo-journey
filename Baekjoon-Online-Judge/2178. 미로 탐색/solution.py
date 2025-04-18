# 2178. 미로 탐색
# 메모리 34,976 kb / 실행시간 100 ms

import sys
from collections import deque

sys.stdin = open("./sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[N*M+1] * M for _ in range(N)] # 각 위치에 도달하기 위한 최소 이동 횟수 저장
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1 # 시작 위치 방문 처리

    for x in range(N):
        for y in range(M):
            if maze[x][y] == 1:
                q.append((x, y))

    # BFS 탐색
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < M and maze[new_x][new_y] == 1:
                if visited[new_x][new_y] > visited[x][y] + 1:
                    visited[new_x][new_y] = visited[x][y] + 1
                    q.append((new_x, new_y))

    print(visited[N-1][M-1])







