# 1920. 수 찾기
# 메모리 48,604kb / 실행시간 388ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

def check(elem):
    l, r = 0, N-1
    if elem > arr[r] or elem < arr[l]:
        return '0'
    
    while l <= r: 
        m = (l + r) // 2
        if arr[m] == elem:
            return '1'
        elif arr[m] < elem:
            l = m + 1
        else:
            r = m - 1
    return '0'

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    M = int(input())
    inspection = list(map(int, input().split()))
    
    print('\n'.join(map(check, inspection)))











