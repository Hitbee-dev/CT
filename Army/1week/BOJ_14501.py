# 2022/11/29
# 백준 14501번 퇴사

# 퇴사까지 남은 날 = N
N = int(input())
# 남은 일자 동안 잡혀있는 상담기간, 상담금액
info = [list(map(int, input().split())) for _ in range(N)]
used_day = [0] * N
INF = 1e9
max_money = -INF


def get_max_money(cnt, money):
    global max_money
    if cnt == N:
        if money > max_money:
            max_money = money
        return
    for do in range(2):
        # 상담을 안 하는 경우
        if do == 0:
            get_max_money(cnt+1, money)
        # 상담을 하는 경우
        else:
            # 이미 그 날에 상담이 진행 중인 경우
            if used_day[cnt] == 1:
                continue
            # 상담기간을 더한 날이 퇴사 날보다 큰 경우
            if cnt + info[cnt][0] > N:
                continue
            for use in range(cnt, cnt + info[cnt][0]):
                if use <= N-1:
                    # 상담기간 만큼 사용 일자 True 처리
                    used_day[use] = 1
            get_max_money(cnt+1, money+info[cnt][1])
            for use in range(cnt, cnt + info[cnt][0]):
                if use <= N-1:
                    used_day[use] = 0


get_max_money(0, 0)
print(max_money)
