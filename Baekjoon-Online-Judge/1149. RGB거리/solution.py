# 1149. RGB거리
# 메모리 33,432kb / 실행시간 36ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*3 for _ in range(N)]
    dp[0] = cost[0]
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    print(min(dp[N-1]))


    











