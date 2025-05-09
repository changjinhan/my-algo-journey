# 2105. [모의 SW 역량테스트] 디저트 카페
# 메모리 94,976kb / 실행시간 1,820ms
import sys
sys.stdin = open('sample_input.txt', 'r')

dr = [1, 1, -1, -1]  # ↘ ↙ ↖ ↗
dc = [1, -1, -1, 1]

def dfs(start_r, start_c, r, c, direction, count, visited):
    global max_count

    for d in range(direction, direction + 2):  # 방향은 현재 or 다음으로만 가능 (최대 3번 꺾음)
        if d >= 4:
            continue
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N:
            if nr == start_r and nc == start_c and count >= 4:
                max_count = max(max_count, count)
                return
            if desserts[nr][nc] not in visited:
                visited.add(desserts[nr][nc])
                dfs(start_r, start_c, nr, nc, d, count + 1, visited)
                visited.remove(desserts[nr][nc])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1

    for i in range(0, N-2):
        for j in range(1, N-1):
            visited = set()
            visited.add(desserts[i][j])
            dfs(i, j, i, j, 0, 1, visited)

    print(f"#{tc} {max_count}")
