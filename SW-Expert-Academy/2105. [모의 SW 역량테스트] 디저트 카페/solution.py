# 2105. [모의 SW 역량테스트] 디저트 카페
# 메모리 73,344kb / 실행시간 580ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def bfs(sr, sc):
    max_local = -1
    q = deque()
    visited = set()
    visited.add(desserts[sr][sc])
    q.append((sr, sc, sr, sc, 0, visited)) # 시작 위치, 현재 위치, 방향, 방문 디저트
    while q:
        sr, sc, r, c, d, visited = q.popleft()
        for nd in [d, d + 1]:  # 현재 방향 그대로 or 다음 방향으로만 이동
            if nd >= 4:
                continue
            nr = r + dr[nd]
            nc = c + dc[nd]
            if 0 <= nr < N and 0 <= nc < N:
                if nr == sr and nc == sc and len(visited) >= 4:
                    max_local = max(max_local, len(visited))
                    continue
                if desserts[nr][nc] not in visited:
                    new_visited = visited.copy()
                    new_visited.add(desserts[nr][nc])
                    q.append((sr, sc, nr, nc, nd, new_visited))
    return max_local

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_count = -1
    for r in range(0, N-2):
        for c in range(1, N-1):
            count = bfs(r, c)
            max_count = max(max_count, count)
    print(f'#{tc} {max_count}')