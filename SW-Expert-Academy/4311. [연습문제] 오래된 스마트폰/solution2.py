# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys
from collections import deque

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("./sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
op_dict = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
}


def solve():
    for test_case in range(1, T + 1):
        N, O, M = map(int, input().split())
        arr = list(map(int, input().split()))
        ops = [op_dict[i] for i in list(map(int, input().split()))]
        W = int(input())
        visited = [M+1] * 1000

        # 숫자만 눌러서 만들 수 있는 값 기록
        q = deque()
        for d in arr:
            visited[d] = 1
            q.append(d)
        
        # 여러 자리수 만들기
        only_nums = []
        for _ in range(2, 4):  # 최대 3자리까지
            for num in range(1000):
                if visited[num] == _ - 1:
                    for d in arr:
                        val = num * 10 + d
                        if val < 1000 and visited[val] > _:
                            visited[val] = _
                            only_nums.append(val)
                            q.append(val)

        # 숫자만 눌러서 만들 수 있으면 종료
        if visited[W] <= M:
            print(f'#{test_case} {visited[W]}')
            continue


        while q:
            cur = q.popleft()
            for num in only_nums:
                click_cnt = visited[cur] + 1 + len(str(num)) # 연산자 + 숫자 누르는 횟수
                if click_cnt + 1 > M: # = 누르는 횟수 반영
                    continue
                for op in ops:
                    val = None
                    if op == '+':
                        val = cur + d
                    elif op == '-':
                        val = cur - d
                    elif op == '*':
                        val = cur * d
                    elif op == '/':
                        if d == 0:
                            continue
                        val = cur // d
                    if val is not None and 0 <= val < 1000:
                        if visited[val] > click_cnt:
                            visited[val] = click_cnt
                            q.append(val)

        # 정답 출력
        if visited[W] <= M - 1:
            print(f'#{test_case} {visited[W] + 1}')
        else:
            print(f'#{test_case} -1')

if __name__ == "__main__":
    solve()