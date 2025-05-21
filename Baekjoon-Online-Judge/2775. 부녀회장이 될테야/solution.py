# 2772. 부녀회장이 될테야
# DFS: 메모리 32,412kb / 실행시간 32ms

import sys
sys.stdin = open("./sample_input.txt", "r")

dp = [[0]*14 for _ in range(15)]
dp[0] = list(range(1, 15))
for i in range(1, 15):
    for j in range(14):
        dp[i][j] = sum(dp[i-1][:j+1])
T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])