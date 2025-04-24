import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

def bfs(waper):
    visited = set()
    q = deque()
    q.append((0, 0, visited))
    max_chips = 0

    while q:
        hidx, widx, visited = q.popleft()
        if widx >= W - 1:
            continue
        if hidx == H - 1:
            max_chips = max(max_chips, len(visited) // 4)
            # print(visited)
            continue

        if hidx < H - 1 and widx < W - 1:
            can_place = not waper[hidx][widx] and not waper[hidx][widx+1] \
                        and not waper[hidx+1][widx] and not waper[hidx+1][widx+1] \
                        and (hidx, widx) not in visited
            if can_place:
                new_visited = visited.copy()
                new_visited.add((hidx, widx))
                new_visited.add((hidx, widx+1))
                new_visited.add((hidx+1, widx))
                new_visited.add((hidx+1, widx+1))
            
                if widx == W - 2:
                    q.append((hidx + 1, 0, new_visited))
                else:
                    q.append((hidx, widx + 2, new_visited))
            
            if widx == W - 2:
                q.append((hidx + 1, 0, visited))
            else:
                q.append((hidx, widx + 1, visited))

    return max_chips


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    waper = [list(map(int, input().split())) for _ in range(H)]
    result = bfs(waper)
    print(f'#{tc} {result}')