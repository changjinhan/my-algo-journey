# 20291. 파일 정리
# 메모리 45,956 kb / 실행시간  216ms

import sys
from collections import Counter

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # N = int(sys.stdin.readline().strip()) # 백준 제출용
    ext_list = []
    for _ in range(N):
        ext = input().split('.')[-1]
        # ext = sys.stdin.readline().strip().split('.')[-1] # 백준 제출용
        ext_list.append(ext)
    ext_counts = Counter(ext_list).most_common()
    sorted_count = sorted(ext_counts, key=lambda x: x[0])
    for k, v in sorted_count:
        print(k, v)














