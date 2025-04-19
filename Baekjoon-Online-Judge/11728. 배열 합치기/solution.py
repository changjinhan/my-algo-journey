# 11728. 배열 합치기
# 투 포인터: 메모리 312,640kb / 실행시간 1,424ms
# 힙 병합: 메모리 295,936kb / 실행시간 1,064ms

import sys
import heapq

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    
    # 투 포인터 풀이
    # l, r = 0, 0
    # result = []

    # # O(N+M)
    # while l < N and r < M:
    #     if arr_A[l] <= arr_B[r]:
    #         result.append(arr_A[l])
    #         l += 1
    #     else:
    #         result.append(arr_B[r])
    #         r += 1
    
    # if l < N:
    #     result.extend(arr_A[l:])
    # if r < M:
    #     result.extend(arr_B[r:])

    # 힙 병합 풀이
    result = heapq.merge(arr_A, arr_B)
    
    print(' '.join(map(str, result))) # for문 돌면서 print 하지말고 join 사용하기
    
            














