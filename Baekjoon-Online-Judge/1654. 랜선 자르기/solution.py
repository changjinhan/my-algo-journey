# 1654. 랜선 자르기
# 메모리 33,432kb / 실행시간 68ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

def total_count(m):
    return sum(map(lambda x: x // m, line_lens))

for test_case in range(1, T+1):
    K, N = list(map(int, input().split()))
    line_lens = list(int(input()) for _ in range(K))
    line_lens = sorted(line_lens)
    max_len = line_lens[-1]

    l, r = 1, max_len

    while l <= r:
        m = (l + r) // 2
        if total_count(m) >= N:
            l = m + 1
        else:
            r = m - 1

    print(min(l, r))


    











