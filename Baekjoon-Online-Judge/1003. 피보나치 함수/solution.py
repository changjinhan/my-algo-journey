# 1003. 피보나치 함수
# 메모리 32,412kb / 실행시간 36ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

dp = [(1,0), (0,1)]
for i in range(2, 41):
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp.append((zero, one))
    

for test_case in range(1, T+1):
    N = int(input())
    for _ in range(N):
        num = int(input())
        print(dp[num][0], dp[num][1])

    











