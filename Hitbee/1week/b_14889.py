'''
축구하려고 모인 N명은 무조건 짝수
절반을 나눠서 스타트팀과 링크팀으로 나눔
번호를 1 ~ N까지로 배정함
능력치를 조사해봤더니 i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치의 합이다
4
12 13 14 | 23 24 34
34 24 23 | 14 13 12

6
123 124 125 126 134 135 136 145 146 156 | 234 235 236 245 246 256 345 346 356 456
456 356 346 345 256 246 245 236 235 234 | 156 146 145 136 135 134 126 125 124 123

N = 4이고 S는 아래와 같은 경우를 보자.
i/j 1   2   3   4
1       1   2   3
2   4       5   6
3   7   1       2
4   3   4   5       
예를 들어, 1, 2번이 스타트팀 3, 4번이 링크팀에 속한 경우에 두 팀의 능력치는 아래와 같다.
스타트팀:   S12 + S21 = 1 + 4 = 5
링크팀:     S34 + S43 = 2 + 5 = 7

1, 3번이 스타트팀 2, 4번이 링크팀에 속하면 두 팀의 능력치는 아래와 같다.
스타트팀:   S13 + S31 = 2 + 7 = 9
링크팀:     S24 + S42 = 6 + 4 = 10

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 팀의 능력치의 차이를 최소로 하려고 한다.
위의 예제와 같은 경우에는 1, 4번이 스타트팀, 2, 3번이 링크팀에 속하면 차이가 0이 되어 최소값이다.

입력
첫째줄에 N(4 <= N <= 20)
둘째줄에 N개의 줄에 S가 주어진다.
Sii는 항상 0이고, 나머지는 1보다 크거나 같고, 100보다도 작거나 같은 정수이다.

또 완전탐색, dp인데?
'''

import sys
from itertools import *
input = sys.stdin.readline

def dp_table(data):
    x, y = data
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = S[x][y] + S[y][x]
    return dp[x][y]

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
'''
N = 4
S = [[0, 1, 2, 3],
     [4, 0 ,5 ,6],
     [7, 1, 0, 2],
     [3, 4, 5, 0]]
'''
'''
N = 6
S = [[0, 1, 2, 3, 4, 5],
     [1, 0, 2, 3, 4, 5],
     [1, 2, 0, 3, 4, 5],
     [1, 2, 3, 0, 4, 5],
     [1, 2, 3, 4, 0, 5],
     [1, 2, 3, 4, 5, 0]]
'''
# 팀의 능력치를 저장해 둘 DP 테이블 선언
dp = [[0] * N for _ in range(N)]
check = [_ for _ in range(N)]

# 나올 수 있는 경우의 수 구하기(Number of Case)
noc = list(combinations(check, N//2))

# 스타트팀의 경우의 수
start = noc[:len(noc)//2]

# 링크팀의 경우의 수
end = list(reversed(noc))[:len(noc)//2]

result = 1e9
sbuf, ebuf = [], []
for s, e in zip(start, end):
    for st, et in zip(list(combinations(s, 2)), list(combinations(e, 2))):
        sbuf.append(dp_table(st))
        ebuf.append(dp_table(et))
    result = min(result, abs(sum(sbuf) - sum(ebuf)))
    sbuf.clear()
    ebuf.clear()
print(result)