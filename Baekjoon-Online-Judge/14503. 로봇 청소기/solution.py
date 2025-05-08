# 14503. 로봇 청소기
# 메모리 32,412kb / 실행시간 44ms

import sys
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room_state = [list(map(int, input().split())) for _ in range(N)]
    
    clean_count = 0
    running = True
    directions = {0: [(-1, 0), (1, 0)], 1: [(0, 1), (0, -1)], 2: [(1, 0), (-1, 0)], 3: [(0, -1), (0, 1)]}
    while running:
        if room_state[r][c] == 0:
            room_state[r][c] = -1 # cleaned
            clean_count += 1

        if room_state[r-1][c] != 0 and room_state[r][c+1] != 0 and room_state[r+1][c] != 0 and room_state[r][c-1] != 0:
            if room_state[r + directions[d][1][0]][c + directions[d][1][1]] != 1:
                r += directions[d][1][0]
                c += directions[d][1][1]
            else:
                running = False
        else:
            if d == 0:
                d = 3
            else:
                d -= 1
            if room_state[r + directions[d][0][0]][c + directions[d][0][1]] == 0:
                r += directions[d][0][0]
                c += directions[d][0][1]

    print(clean_count)













