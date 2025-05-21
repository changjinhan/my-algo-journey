# 2839. 설탕 배달
# 메모리 32,412kb / 실행시간 40ms

import sys
sys.stdin = open("./sample_input.txt", "r")

dp = [float('inf')] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, 5001):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(dp[N] if dp[N] != float('inf') else -1)