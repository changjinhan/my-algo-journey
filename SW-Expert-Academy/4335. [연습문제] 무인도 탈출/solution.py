import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    boxes = [tuple(map(int, input().split())) for _ in range(N)]
    rotations = []
    for idx, (x, y, z) in enumerate(boxes):
        # 박스 놓는 방법은 높이 기준으로 3가지
        for a, b, c in [(x, y, z), (y, z, x), (z, x, y)]:
            rotations.append((max(a, b), min(a, b), c, idx))

    rotations = sorted(rotations, key=lambda r: r[0]*r[1]) # 바닥 넓이 기준 오름차순 정렬
    dp = [rotations[i][2] for i in range(3*N)] # 처음 쌓았을 때 높이
    used_indices = [{rotations[i][3]} for i in range(3*N)] # 처음 쌓았을 때 사용한 박스 번호
    
    for i in range(3*N):
        w1, l1, h1, idx1 = rotations[i]
        for j in range(i):
            w2, l2, h2, idx2 = rotations[j]
            if w1 >= w2 and l1 >= l2 and idx1 not in used_indices[j]:
                if dp[i] < dp[j] + h1:
                    dp[i] = dp[j] + h1
                    used_indices[i] = used_indices[j].copy()
                    used_indices[i].add(idx1)

    print(f'#{test_case} {max(dp)}')

