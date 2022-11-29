'''
총 N개의 시험장이 있고, 각각의 시험장마다 응시자가 있다.
i번 시험장에 있는 응시자의 수는 Ai명이다.

감독관은 총감독관과 부감독관으로 두 종류가 있다.
한 시험장에서 감시할 수 있는 응시자의 수가 B명이고,
부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.

각각의 시험장에 총감독관은 오직 1명만 있어야 하고,
부감독관은 여러명 있어도 된다.

각 시험장 마다 응시생들을 모두 감시해야한다.
이때, 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 시험장의 개수 N(1 <= N <= 1,000,000)이 주어진다.
둘째 줄에는 각 시험장에 있는 응시자의 수 Ai(1 <= Ai <= 1,000,000)가 주어진다.
셋째 줄에는 B와 C가 주어진다. (1 <= B, C <= 1,000,000)

출력
각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력한다.

> 데이터의 개수가 100만개 이상이니 O(N)으로 풀어야 한다.
-> 2중 for문은 사용 불가능 하다는 뜻

1. 총 감독관이 감시할 수 있는 응시자의 수를 먼저 뺀다.
2. 시험관의 개수만큼 반복 진행
3. 시험관의 개수만큼 총 감독관의 수가 필요하므로 count에 더해줌
3. 각 시험관에 남은 학생 수 만큼 나눠서 몫과 나머지를 구함
4. 몫은 그대로 count에 더해주고(감독에 필요한 부 감독관의 수)
5. 나머지가 0이 아니라면 부 감독관이 1명 더 필요하니 count += 1
'''

import sys

def min_student(ab):
    af = [a - B for a in ab]
    # 총 감독관이 감시할 수 있는 응시자의 수를 각 시험장에 있는 응시자들에서 제외
    count  = len(af)
    for a in af:
        if a > 0:
        # 이거 하나 안 넣어줬다고 테스트 케이스 통과가 안됨
        # 왜냐, 학생 수 보다 총 감독관이 감시할 수 있는 응시자의 수가 많으면 -값이 들어가는데,
        # 이를 % 나머지 연산 하게 되면 0이 아닌 다른 상수가 나올 수 있기 때문
            count += a//C
            if a % C != 0:
                count += 1
    return count

input = sys.stdin.readline
N = int(input().strip())
# 시험장의 개수
A = list(map(int, input().split()))
# 각 시험장에 있는 응시자의 수
B, C = map(int, input().split())
# 총 감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이다.
# 부 감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.

print(min_student(A))