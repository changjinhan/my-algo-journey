# 1010. 다리 놓기
# 메모리 32,412kb / 실행시간 124ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dp = [[0]*29 for _ in range(29)]
    dp[0] = [i for i in range(1, 30)]
    for i in range(1, 30):
        for j in range(i, 29):
            dp[i][j] = sum(dp[i-1][:j])
    print(dp[N-1][M-1])