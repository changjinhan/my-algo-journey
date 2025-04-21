# 9095. 1, 2, 3 더하기
# 메모리 32,412kb / 실행시간 36ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

C = [0] * 11
C[0] = 1
C[1] = 2
C[2] = 4
for n in range(3, 11):
    C[n] = C[n-1] + C[n-2] + C[n-3]

for test_case in range(1, T+1):
    N = int(input())
    for _ in range(N):
        num = int(input())
        print(C[num-1])





