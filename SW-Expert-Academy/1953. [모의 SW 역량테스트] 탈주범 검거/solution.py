# 1953. [모의 SW 역량테스트] 탈주범 검거
# 메모리 60,800kb / 실행시간 121ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

def bfs(r, c, l):
    count = 0
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((r, c, l))
    visited[R][C] = True
    while q:
        r, c, l = q.popleft()
        count += 1
        if l == L:
            continue
        tn = tunnels[r][c]
        for dr, dc in out_directions[tn]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and tunnels[nr][nc] !=0 and not visited[nr][nc]:
                next_tn = tunnels[nr][nc]
                if (-dr, -dc) in out_directions[next_tn]:
                    visited[nr][nc] = True
                    q.append((nr, nc, l+1))
    return count

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnels = [list(map(int, input().split())) for _ in range(N)]
    out_directions = {1: [(-1, 0), (1, 0), (0, -1), (0, 1)], # 상하좌우
                  2: [(-1, 0), (1, 0)], # 상하
                  3: [(0, -1), (0, 1)], # 좌우
                  4: [(-1, 0), (0, 1)], # 상우
                  5: [(1, 0), (0, 1)], # 하우
                  6: [(1, 0), (0, -1)], # 하좌
                  7: [(-1, 0), (0, -1)]} # 상좌
    count = bfs(R, C, 1)
    print(f'#{tc} {count}')