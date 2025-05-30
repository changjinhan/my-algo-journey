# 12865. 평범한 배낭
# 메모리 230,376kb / 실행시간 4,004ms

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for j in range(K + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    print(dp[N][K])
    
            














