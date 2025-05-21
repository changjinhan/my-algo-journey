# 1932. 정수 삼각형
# 메모리 43,372kb / 실행시간 124ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    triangle = [[0]*N for _ in range(N)]
    for i in range(N):
        triangle[i][:i+1] = list(map(int, input().split()))
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = triangle[0][0]
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    print(max(dp[N-1]))











