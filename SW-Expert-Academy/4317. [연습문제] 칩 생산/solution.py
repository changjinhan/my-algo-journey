# 4317. [연습문제] 칩 생산
# 메모리 67,712kb / 실행시간 152ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

def dfs(r, c, num, mask): 
    global max_chips
    if r >= H-1:
        if num <= visited[mask][c]: # 이전보다 칩을 더 못 놓았으면 가지치기
            return
        else:
            visited[mask][c] = num
            dfs(0, c+1, num, 0) # 다음 열로 이동, mask 초기화
            return
    elif c >= W-1:
        max_chips = max(max_chips, num)
        return
     
    if waper[r+1][c] or waper[r+1][c+1]: # 아래칸 둘 중 하나 막혀있으면 칩 못 놓음
        dfs(r+2, c, num, mask)           # 칩 안 놓고 2칸 건너뜀 (칩의 세로 크기)
    elif waper[r][c] or waper[r][c+1]:   # 윗칸 둘 중 하나 막혀있어도 못 놓음
        dfs(r+1, c, num, mask)           # 칩 안 놓고 한 칸만 이동
    else:
        # 4칸이 모두 비었으면 칩을 놓아본다
        waper[r+1][c] = waper[r+1][c+1] = waper[r][c] = waper[r][c+1] = 1
        dfs(r+2, c, num+1, mask | (1 << r)) # 칩 하나 놓고 진행
        waper[r+1][c] = waper[r+1][c+1] = waper[r][c] = waper[r][c+1] = 0 # 상태 복원 (백트래킹)
        dfs(r+1, c, num, mask) # 칩을 안 놓는 분기


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    waper = [list(map(int, input().split())) for _ in range(H)]
    visited = [[-1] * W for _ in range(1 << H)]
    max_chips = 0
    dfs(0, 0, 0, 0)
    print(f'#{tc} {max_chips}')