''' 라면 사기(Small)
교준이네 집 주변에는 N개의 라면 공장이 있다.
각 공장은 1번부터 N번까지 차례대로 번호가 부여되어 있다.
교준이는 i번 공장에서 정확하게 Ai개 라면을 구매하고자 한다.

교준이는 아래의 세가지 방법으로 라면을 구매할 수 있다.
1. i번 공장에서 라면을 하나 구매한다.(이 경우 비용은 3원이 든다.)(i <= i <= N)
2. i번 공장과(i+1)번 공장에서 각각 라면을 하나씩 구매한다.(이 경우 비용은 5원이 든다.)(i <= i <= N-1)
3. i번 공장과(i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다.(이 경우 비용은 7원이 든다.)(i <= i <= N-2)

최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성하시오.
'''

# 라면 공장의 개수를 의미하는 자연수 N
import sys

def search_data(idx, a, value):
    # 3자리를 한번에 봤는데 0이 없다면
    if idx < N-2 and 0 not in a[idx:3]:
        min_buf = min(a[idx:3])
        for na in range(idx, idx+3):
            a[na] = a[na] - min_buf
        return idx, a, value+min_buf*7
    # 2자리를 한번에 봤는데 0이 없다면
    if idx < N-1 and 0 not in a[idx:2]:
        min_buf = min(a[idx:2])
        for na in range(idx, idx+2):
            a[na] = a[na] - min_buf
        return idx, a, value+min_buf*5
    # 1자리를 봤는데 0이 없다면
    if 0 != a[idx]:
        buf = a[idx]*3
        a[idx] = 0
        return idx, a, buf
    return idx, a, value

def buy(idx, a, value):
    # 마지막이라면
    if idx == N:
        print(f"값: {value}")
        return
    idx, a, value = search_data(idx, a, value)
    return buy(idx+1, a, value) 



        

# input = sys.stdin.readline
# N = int(input())
# A = list(map(int, input().split()))

# N = 3
# A = [1, 0, 1]

N = 5
A = [1, 1, 1, 0, 2, 0]

# 히든 테스트 케이스
# N = 4
# A = [1, 2, 1, 1]

dp = [0] * (N)

buy(0, A, 0)