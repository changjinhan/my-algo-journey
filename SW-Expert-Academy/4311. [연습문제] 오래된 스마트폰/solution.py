# 4311. [연습문제] 오래된 스마트폰
# 본 문제는 외부 라이브러리 사용불가 => 메모리 62,464 kb / 실행시간 361 ms
# 12094번 문제에서는 외부 라이브러리 사용 가능 => (deque 사용 시) 메모리 61,312 kb / 실행시간 197 ms

import sys
# from collections import deque

sys.stdin = open("./sample_input.txt", "r")

T = int(input())

op_dict = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
}

def recur(cur, val):
    if cur == 3:
        return
    for d in arr:
        num = 10 * val + d
        if num < 1000 and visited[num] > cur + 1:
            visited[num] = cur + 1
            only_nums.append(num)
            q.append(num)
            recur(cur + 1, num)


for test_case in range(1, T + 1):
    N, O, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ops = [op_dict[i] for i in list(map(int, input().split()))]
    W = int(input())
    visited = [M+1] * 1000

    # 숫자만 눌러서 만들 수 있는 값 기록
    # q = deque()
    q = []
    only_nums = []
    recur(0, 0)

    # 숫자만 눌러서 만들 수 있으면 종료
    if visited[W] <= M:
        print(f'#{test_case} {visited[W]}')
        continue
    
    # 연산자 + 숫자 눌러서 만들 수 있는 값 기록
    while q:
        # cur = q.popleft()
        cur = q.pop(0)
        for num in only_nums:
            click_cnt = visited[cur] + 1 + len(str(num)) # 연산자 + 숫자 누르는 횟수
            if click_cnt + 1 > M: # = 누르는 횟수 반영
                continue
            for op in ops:
                val = None
                if op == '+':
                    val = cur + num
                elif op == '-':
                    val = cur - num
                elif op == '*':
                    val = cur * num
                elif op == '/':
                    if num == 0:
                        continue
                    val = cur // num
                if val is not None and 0 <= val < 1000:
                    if visited[val] > click_cnt:
                        visited[val] = click_cnt
                        q.append(val)
    
    # 정답 출력
    if visited[W] <= M - 1:
        print(f'#{test_case} {visited[W] + 1}')
    else:
        print(f'#{test_case} -1')
