# 1932. 정수 삼각형
# 메모리 36,504kb / 실행시간 104ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().strip().split())) for _ in range(N)]
    dp = arr
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    print(max(dp[N-1]))











