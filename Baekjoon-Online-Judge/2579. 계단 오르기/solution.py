# 2579. 계단 오르기
# 메모리 32,412kb / 실행시간 36ms

import sys
from collections import deque

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    S = [int(input()) for _ in range(N)]
    H = [0] * N
    
    if N == 1:
        print(S[0])
    elif N == 2:
        print(S[0] + S[1])
    elif N == 3:
        print(max(S[0] + S[2], S[1] + S[2]))
    else:
        H[0] = S[0]
        H[1] = S[0] + S[1]
        H[2] = max(S[0] + S[2], S[1] + S[2])
        for n in range(3, N):
            H[n] = max(H[n-3] + S[n-1] + S[n], H[n-2] + S[n])
        print(H[-1])






