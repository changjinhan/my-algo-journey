# 1463. 1로 만들기
# 연결 리스트 풀이: 메모리 71,968kb / 실행시간 752ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [float('inf')] * (N+1)
    dp[-1] = 0
    for i in range(N, -1, -1):
        if i % 3 == 0:
            dp[i // 3] = min(dp[i // 3], dp[i] + 1)
        if i % 2 == 0:
            dp[i // 2] = min(dp[i // 2], dp[i] + 1)
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    print(dp[1])
        












