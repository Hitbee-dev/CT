# 병사 배치하기

'''
N명의 병사가 무작위로 나열되어 있다.
각 병사는 특정한 값의 전투력을 보유하고 있다.

병사를 배치할 떄는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다.
앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.

또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다.
그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.
'''

'''
1 2 3 4 5 6 7
15 11 4 8 5 2 4

이 때, 3번 병사와 6번 병사를 열외시키면 내림차순 형태가 되며, 5명이 된다.
이는 남아있는 병사의 수가 최대가 되도록 하는 방법이다.

1 2 4 5 7
15 11 8 5 4

병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램을 작성하라.
'''

N = 7
nights = [15, 11, 4, 8, 5, 2, 4]
nights.reverse()

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nights[j] < nights[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))