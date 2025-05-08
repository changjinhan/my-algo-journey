# 14889. 스타트와 링크
# 메모리 57,548kb / 실행시간 3,008ms

import sys
import itertools
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stats = [list(map(int, input().split())) for _ in range(N)]
    r = N // 2
    NCr = list(itertools.combinations(range(N), r))
    num_comb = len(NCr)
    min_diff = float('inf')
    for i in range(num_comb//2):
        a_team = NCr[i]
        b_team = NCr[num_comb - 1 - i]
        a_team_stat = b_team_stat = 0
        for a_team_pair in list(itertools.permutations(a_team, 2)):
            a_team_stat += stats[a_team_pair[0]][a_team_pair[1]]
        for b_team_pair in list(itertools.permutations(b_team, 2)):
            b_team_stat += stats[b_team_pair[0]][b_team_pair[1]]
        diff = abs(a_team_stat - b_team_stat)
        min_diff = min(min_diff, diff)
        if min_diff == 0:
            break

    print(min_diff)











