# 11726. 2xn 타일링
# 메모리 32,544kb / 실행시간 36ms

import sys
from collections import deque

sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        result = 1
    elif N == 2:
        result = 2
    else:
        dp = [0] * N
        dp[0] = 1
        dp[1] = 2
        for i in range(2, N):
            dp[i] = (dp[i - 1] + dp[i - 2])
        result = dp[N-1] % 10007
    print(result)
        
