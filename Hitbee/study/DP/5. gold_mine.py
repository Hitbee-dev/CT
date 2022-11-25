# 금광

'''
N X M 크기의 금광이 있다.
금광은 1 X 1크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있다.

채굴자는 첫번째 열부터 출발하여 금을 캐기 시작한다.
맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.
이후에 m-1번에 걸쳐 매번 오늘쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라.

1 3 3 2
2 1 4 1
0 6 4 7

-> sum(2 6 4 7) = 19
'''

'''
첫째줄에 테스트케이스 T가 입력됨 (1 <= T <= 1000)

매 테스트 케이스 첫째 줄에 N과 M이 공백으로 구분되어 입력 됨 (1 <= n, m <= 20)
둘째줄에 N X M개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됨 (1 <= 각 위치에 매장된 금의 개수 <= 100)

테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다.
각 테스트 케이스는 줄바꿈을 이용해 구분한다.
'''

# 이동할 수 있는 범위를 지정하지 않았을 때
'''
def gold_mine(n, m, gold):
    start, end = 0, m
    gold_dict = {}
    for i in range(n):
        gold_dict[i] = gold[start:end]
        start, end = (start+m), (end+m)
    print(gold_dict)
    max_gold = [0]*m
    for key, value in gold_dict.items():
        for idx, v in enumerate(value):
            if max_gold[idx] < v:
                max_gold[idx] = v
    print(max_gold)
    return sum(max_gold)

T = 2
N, M = 3, 4
golds = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

print(gold_mine(N, M, golds))

N, M = 4, 4
golds = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]

print(gold_mine(N, M, golds))
'''

# 금광의 모든 위치에 대해 3가지만 고려하면 된다.
'''
1. 왼쪽 위에서 오는 경우
2. 왼쪽 아래에서 오는 경우
3. 왼쪽에서 오는 경우

이 3가지 경우 중, 가장 많은 금을 가지고 있는 경우를 테이블에 갱신 해 주어 문제를 해결
'''

'''
array[i][j] = i행 j열에 존재하는 금의 양
dp[i][j] = i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j-1])
            현재 위치      +      왼쪽 위        왼쪽          왼쪽 아래
'''

def gold_mine(n, m, gold):
    dp = []
    start = 0

    # 이차원 배열로 변환
    for _ in range(n):
        dp.append(gold[start:start+m])
        start += m

    # DP 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for r in dp:
        if result < r[-1]:
            result = r[-1]
    return result

T = 2
N, M = 3, 4
golds = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
print(gold_mine(N, M, golds))

N, M = 4, 4
golds = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]
print(gold_mine(N, M, golds))