# 4340. [연습문제] 파이프 연결
# 메모리 115,136kb / 실행시간 722ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

# 상하좌우
directions = {
    0: (-1, 0), 
    1: (1, 0), 
    2: (0, -1), 
    3: (0, 1)
}
opposite = [1, 0, 3, 2]

# 각 파이프 타입별 가능한 (in_dir, out_dir) 쌍
pipe_dirs = {
    0: [],
    1: [(0, 1), (2, 3)],
    2: [(0, 1), (2, 3)],
    3: [(0, 3), (1, 3), (1, 2), (0, 2)],
    4: [(0, 3), (1, 3), (1, 2), (0, 2)],
    5: [(0, 3), (1, 3), (1, 2), (0, 2)],
    6: [(0, 3), (1, 3), (1, 2), (0, 2)],
}


def bfs(si, sj, ei, ej, start_dir, end_dir):
    queue = deque()
    visited = set()
    queue.append((si, sj, start_dir, 1, visited))
    dij = [[[N * N + 1] * 4 for _ in range(N)] for _ in range(N)] # [N, N, 4] => 해당 위치에서 입력 방향별 최소 거리

    while queue:
        ci, cj, dir_in, dist, visited = queue.popleft()
        if dist > dij[ci][cj][dir_in]: # 해당 위치, 방향에서 최솟값보다 크면 탐색 종료
            continue
        
        pipe_type = maps[ci][cj]
        if (ci, cj) == (ei, ej):
            for p_dir in pipe_dirs[pipe_type]:
                if dir_in in p_dir and end_dir in p_dir:
                    return dist       
        visited.add((ci, cj))
        dij[ci][cj][dir_in] = dist

        for p_dir in pipe_dirs[pipe_type]:
            if dir_in in p_dir:
                for p in p_dir:
                    if dir_in == p:
                        continue
                    di, dj = directions[p]
                    ni, nj = ci + di, cj + dj
                    if (0 <= ni < N) and (0 <= nj < N) and maps[ni][nj] != 0 and (ni, nj) not in visited:
                        queue.append((ni, nj, opposite[p], dist+1, set(visited))) # set을 복사해서 새 set을 만듦
    
    return float('inf')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    l_start = bfs(0, 0, N-1, N-1, 2, 3)
    r_start = bfs(N-1, N-1, 0, 0, 3, 2)
    
    print(f"#{tc} {min(l_start, r_start)}")