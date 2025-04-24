# 4013. [모의 SW 역량테스트] 특이한 자석
# 메모리 59,136kb / 실행시간 95ms
import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def bfs(m_idx, dir):
    q = deque()
    q.append([m_idx, dir])
    visited = set([])
    while q:
        m_idx, dir = q.popleft()
        visited.add((m_idx, dir))
        # right check
        if 0 <= m_idx <= 2:
            if magnets[m_idx][2] != magnets[m_idx+1][6] and (m_idx + 1, -dir) not in visited:
                q.append((m_idx + 1, -dir))
                visited.add((m_idx + 1, -dir))
        # left check
        if 1 <= m_idx <= 3:
            if magnets[m_idx][6] != magnets[m_idx-1][2] and (m_idx - 1, -dir) not in visited:
                q.append((m_idx - 1, -dir))
                visited.add((m_idx - 1, -dir))
    return list(visited)

for tc in range(1, T+1):
    K = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    command = [tuple(map(int, input().split())) for _ in range(K)]

    for m_idx, dir in command:
        rotations = bfs(m_idx-1, dir)
        for (idx, dir) in rotations:
            magnets[idx].rotate(dir)
    
    result = magnets[0][0] * 1 + magnets[1][0] * 2 + magnets[2][0] * 4 + magnets[3][0] * 8
    print(f'#{tc} {result}')