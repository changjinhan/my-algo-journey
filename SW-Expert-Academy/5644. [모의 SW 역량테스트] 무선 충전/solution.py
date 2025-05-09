# 5644. [모의 SW 역량테스트] 무선 충전
# 메모리 62,208kb / 실행시간 182ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

def dfs(cnum, sy, sx, y, x, C):
    charge_map[y][x].add(cnum)
    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < 10 and 0 <= nx < 10 and cnum not in charge_map[ny][nx]:
            if abs(sy - ny) + abs(sx - nx) <= C:
                dfs(cnum, sy, sx, ny, nx, C)

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    track_a = list(map(int, input().split()))
    track_b = list(map(int, input().split()))
    charge_map = [[set() for _ in range(10)] for _ in range(10)]
    performance = {}
    for i in range(A):
        X, Y, C, P = map(int, input().split())
        dfs(i, Y-1, X-1, Y-1, X-1, C)
        if i not in performance:
            performance[i] = P
    pos_a = [(0, 0)] * (M+1)
    pos_b = [(9, 9)] * (M+1)
    dirs = {0: (0,0), 1: (-1,0), 2: (0,1), 3: (1,0), 4:(0,-1)}
    for i in range(1, M+1):
        pos_a[i] = (pos_a[i-1][0] + dirs[track_a[i-1]][0], pos_a[i-1][1] + dirs[track_a[i-1]][1])
        pos_b[i] = (pos_b[i-1][0] + dirs[track_b[i-1]][0], pos_b[i-1][1] + dirs[track_b[i-1]][1])

    amount = 0
    for t in range(0, M+1):
        cand_a = charge_map[pos_a[t][0]][pos_a[t][1]]
        cand_b = charge_map[pos_b[t][0]][pos_b[t][1]]
        
        if not cand_a and not cand_b:
            max_sum = 0
        elif not cand_a and cand_b:
            max_sum = max([performance[n] for n in cand_b])
        elif cand_a and not cand_b:
            max_sum = max([performance[n] for n in cand_a])
        elif cand_a and cand_b:
            max_sum = 0
            for na in cand_a:
                for nb in cand_b:
                    if na == nb:
                        max_sum = max(performance[na], max_sum)
                    else:
                        max_sum = max(performance[na]+performance[nb], max_sum)
        amount += max_sum
    print(f'#{tc} {amount}')
                        
                    

        
        



        

    