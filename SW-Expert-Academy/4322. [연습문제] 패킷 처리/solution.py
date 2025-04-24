# 4320. [연습문제] 패킷 처리
# 메모리 92,544kb / 실행시간 588ms
import sys
from collections import deque

def simulation_bfs(packets, num_cpus):
    q = deque() 
    q.append((0, 0, [0] * num_cpus)) # (pidx, prev_time, wait_times)
    visited = set()

    while q:
        pidx, prev, wtimes = q.popleft()
        if pidx == len(packets): # 모든 패킷이 처리된 경우
            return True
        
        cur, ptime = packets[pidx]
        time_delta = cur - prev
        wtimes = [max(w - time_delta, 0) for w in wtimes] # CPU 별 남은 처리 시간
        wtimes.sort() # 남은 처리 시간 순서가 달라도 같은 경우이므로

        state = (pidx, tuple(wtimes))
        if state in visited:
            continue
        visited.add(state) # 방문한 상태 업데이트
        
        for i in range(num_cpus):
            if wtimes[i] + ptime > 10:
                continue
            new_wtimes = wtimes.copy()
            new_wtimes[i] += ptime
            q.append((pidx+1, cur, new_wtimes))

    return False


sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)] # [(cur, ptime), ...]
    result = -1
    for num_cpus in range(1, 6):
        if simulation_bfs(packets, num_cpus):
            result = num_cpus
            break

    print(f'#{tc} {result}')