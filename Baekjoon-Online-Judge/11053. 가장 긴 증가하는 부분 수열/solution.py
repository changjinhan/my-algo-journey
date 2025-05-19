# 11053. 가장 긴 증가하는 부분 수열
# 메모리 32,412kb / 실행시간 128ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))
    
    



            














