# 2022/11/28
# 백준 13458번 시험 감독


N = int(input())
arr = list(map(int, input().split()))
Master, Sub = map(int, input().split())

answer = 0

for i in range(N):
    # i번째 시험장에 있는 응시생수가 0보다 클 때
    if arr[i] > 0:
        # i번째 시험장에 있는 응시생수에서 총감독관이 감시할 수 있는 인원을 먼저 빼기
        arr[i] -= Master
        answer += 1

    # 총감독관이 감시할 수 있는 인원을 뺐는데도 아직 0보다 크면
    if arr[i] > 0:
        # 남은 응시생수를 부감독관이 감시할 수 있는 Sub 로 나눈 몫을 answer 에 더해주기
        answer += arr[i]//Sub
        # 나머지가 0이 아니면 부감독관 1명 추가로 더해줘야함
        if arr[i] % Sub != 0:
            answer += 1

print(answer)
