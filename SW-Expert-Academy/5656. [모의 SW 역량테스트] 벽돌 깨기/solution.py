# 5656. [모의 SW 역량테스트] 벽돌 깨기
# 메모리 87,808kb / 실행시간 1,144ms
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

# 폭발 함수
def explode(blocks, row, col, W, H):
    if blocks[row][col] == 0:
        return

    visited = [[False] * W for _ in range(H)]
    q = deque()
    q.append((row, col, blocks[row][col]))
    visited[row][col] = True

    while q:
        r, c, power = q.popleft()
        blocks[r][c] = 0  # 벽돌 깨기

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            for i in range(1, power):
                nr = r + dr*i
                nc = c + dc*i
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                    if blocks[nr][nc] > 0:
                        q.append((nr, nc, blocks[nr][nc]))
                        visited[nr][nc] = True

# 중력 적용 함수
def apply_gravity(blocks, W, H):
    for c in range(W):
        new_col = []
        for r in range(H-1, -1, -1):
            if blocks[r][c] != 0:
                new_col.append(blocks[r][c])
        for r in range(H-1, -1, -1):
            if new_col:
                blocks[r][c] = new_col.pop(0)
            else:
                blocks[r][c] = 0

# 남은 벽돌 개수 세기
def count_blocks(blocks):
    return sum(1 for row in blocks for val in row if val != 0)

# DFS 완전탐색
def dfs(n, blocks, W, H):
    global min_result
    remaining = count_blocks(blocks)
    if remaining == 0:
        min_result = 0
        return

    if n == 0:
        min_result = min(min_result, remaining)
        return

    for c in range(W):
        # 해당 열에서 가장 위 벽돌 찾기
        for r in range(H):
            if blocks[r][c] != 0:
                new_blocks = deepcopy(blocks)
                explode(new_blocks, r, c, W, H)
                apply_gravity(new_blocks, W, H)
                dfs(n-1, new_blocks, W, H)
                break  # 한 번만 떨어뜨릴 수 있으므로 break

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    min_result = float('inf')
    dfs(N, blocks, W, H)
    print(f"#{tc} {min_result}")
