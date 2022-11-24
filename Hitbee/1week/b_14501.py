'''
첫째줄: 몇일동안 상담 받을지
둘째줄: (T_i P_i)가 1일부터 N일까지 순서대로 주어짐
T_i는 상담에 필요한 기간
P_i는 상담을 했을 때 받을 수 있는 금액
최대로 이익을 얻을 수 있는 스케줄을 짜는 것이 목표

-> 주어진 시간표 안에서 최대로 이익을 볼 수 있도록 코딩해야함
-> 전체 탐색 문제인듯? 아니, DP였음 ㅋㅋ
'''
import sys

# sys.stdin.readline은 input보다 입력속도가 빠르기 때문에 시간초과 문제에서 해결 방법으로 사용되기도 함.
# input = sys.stdin.readline

# 공백 제거, [3 ] 이런 데이터가 들어와서 문제가 생긴 경우도 있음
# N = int(input().strip())

'''
datas = [["3 10", "5 20", "1 10", "1 20", "2 15", "4 40", "2 200"],
          ["1 1", "1 2", "1 3", "1 4", "1 5", "1 6", "1 7", "1 8", "1 9", "1 10"],
          ["5 50", "5 9", "5 8", "5 7", "5 6", "5 10", "5 9", "5 8", "5 7", "5 6"],
          ["5 50", "4 40", "3 30", "2 20", "1 10", "1 10", "2 20", "3 30", "4 40", "5 50"]]

ns = ["7", "10", "10", "10"]

for n, data in zip(ns, datas):
    count = 0
    for T_P in data:
        T, P = T_P.split(" ")
        print(n, T, P)
'''

N = 7
datas = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

# 1. 데이터를 거꾸로 확인해서 일정에 포함할 수 없는 데이터 제거
for i in range(N, 0, -1):
    T, P = datas[i-1]
    if i + T > N:
        datas.remove(datas[i-1])
    else:
        break

# 2. 나올 수 있는 모든 경우의 수 계산
result = []
fbuf, bbuf, count = 0, 0, 0
for i in range(len(datas)):
    count = datas[i][0]-1
    fbuf = datas[i][1]
    print(count, fbuf)
    for j in range(i+1):
        if count != 0:
            count -= 1
            continue