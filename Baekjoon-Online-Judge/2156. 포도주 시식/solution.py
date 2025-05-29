# 2156. 포도주 시식
# 메모리 33,432kb / 실행시간 40ms

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wines = [int(input()) for _ in range(N)]
    if N == 1:
        print(wines[0])
    elif N == 2:
        print(wines[0] + wines[1])
    else:
        dp = [0] * N
        dp[0] = wines[0]
        dp[1] = wines[0] + wines[1]
        dp[2] = max(wines[0] + wines[2], wines[1] + wines[2], dp[1])
        for i in range(3, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])
        print(dp[N - 1])





