'''
백준이 퇴사할거임
오늘부터 N+1일째 되는 날 퇴사 할거
남은 N일동안 최대한 많은 상담을 해서 퇴직금을 많이 당길꺼임

백준이가 비서에게 최대한 많은 상담을 잡으라고 부탁(임원인듯 ㄷㄷ)
비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아둠(일 개못함)
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어짐
N = 7인 경우 상담 일정표는 아래와 같다.
    1일 2일 3일 4일 5일 6일 7일
Ti  3   5   1   1   2   4   2
Pi  10  20  10  20  15  40  200

1. 이미 날짜로 예약을 잡았기 때문에 순서대로 진행해야 함
2. 만약 3일이 돈을 제일 많이 준다면 1일 2일은 안해도 됨
3. N+1일은 퇴사일이기 때문에 계산 잘해야함

상담을 적절히 잘 해서 백준이가 최대의 수익을 받을 수 있는 프로그램 작성
완전탐색 - DP문제(Memories)
'''

# N = 7
# TP = [[3, 10],[5, 20],[1, 10],[1, 20],[2, 15],[4, 40],[2, 200]]
# N = 10
# TP = [[1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[1, 7],[1, 8],[1, 9], [1, 10]]
# N = 10
# TP = [[5, 10],[5, 9],[5, 8],[5, 7],[5, 6],[5, 10],[5, 9],[5, 8],[5, 7],[5, 6]]

import sys
input = sys.stdin.readline

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i + TP[i][0] > N:
        dp[i] = dp[i+1]
        # continue가 아닌 dp[i+1]을 넣어줘야 하는 이유는 마지막 끝에만 최댓값이 있는 것이 아니라
        # 중간에 최댓값(범위를 벗어나는 값)이 있으면 0이기 때문에 dp[i+1]로 다음 인덱스 값을 줘야함
    else:
        dp[i] = max(dp[i+1], TP[i][1] + dp[i + TP[i][0]])
        '''
        dp[4](15)   dp[5](0),    15   + dp[4 + 2](0)
        dp[3](35)   dp[4](15),   20   + dp[3 + 1](15)
        dp[2](45)   dp[3](35),   10   + dp[2 + 1](35)
        dp[1](45)   dp[2](45),   20   + dp[1 + 5](0)
        dp[0](45)   dp[1](45),   10   + dp[0 + 3](35)
        '''
print(dp[0])