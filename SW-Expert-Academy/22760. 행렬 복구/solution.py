# 22760. 행렬 복구 (D5)
# 메모리 86,656kb / 실행시간 248ms
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input().split()) for _ in range(2*N)]
    A = [[0] * N for _ in range(N)]
    firstnum_dic = {}
    for i in range(2*N):
        firstnum = matrix[i][0]
        if firstnum in firstnum_dic:
            firstnum_dic[firstnum].append(matrix[i])
            firstrow_start = firstnum
        else:
            firstnum_dic[firstnum] = [matrix[i]]

    print(' '.join(firstnum_dic[firstrow_start][0])) # A[0]
    for sn in firstnum_dic[firstrow_start][1][1:]:
        print(' '.join(firstnum_dic[sn][0])) # A[1] ~ A[N-1]
    
    