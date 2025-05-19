# 1912. 연속합
# 메모리 39,096kb / 실행시간 88ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_sum = [0] * N
    max_sum[0] = max_ending = arr[0]
    for i in range(1, N):
        max_ending = max(arr[i], max_ending + arr[i])
        max_sum[i] = max(max_sum[i-1], max_ending)
    print(max_sum[N-1])










