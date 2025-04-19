# 11286. 절댓값 힙
# 메모리  36,776kb / 실행시간  128ms

import sys
import heapq

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # N = int(sys.stdin.readline().strip()) # 백준 제출용
    pos_heap = []
    neg_heap = []
    for _ in range(N):
        x = int(input())
        # x = int(sys.stdin.readline().strip()) # 백준 제출용

        if x != 0: # push
            if x > 0:
                heapq.heappush(pos_heap, x)
            else:
                heapq.heappush(neg_heap, -x)
        else: # pop
            if not pos_heap and not neg_heap:         # 둘다 비어 있는 경우
                print(0)
            elif pos_heap and not neg_heap:           # 양수 힙만 있는 경우
                print(heapq.heappop(pos_heap))
            elif neg_heap and not pos_heap:           # 음수 힙만 있는 경우
                print(-heapq.heappop(neg_heap))
            else:                                     # 둘다 채워져 있는 경우
                min_pos = heapq.heappop(pos_heap)
                min_neg = heapq.heappop(neg_heap)
                if min_pos > min_neg:
                    print(-min_neg)
                    heapq.heappush(pos_heap, min_pos)
                elif min_pos < min_neg:
                    print(min_pos)
                    heapq.heappush(neg_heap, min_neg)
                else:
                    print(-min_neg)
                    heapq.heappush(pos_heap, min_pos)
    
            














