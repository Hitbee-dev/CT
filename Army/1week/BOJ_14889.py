# 2022/11/30
# 백준 14889번 스타트와 링크

# 격자 크기 N * N
N = int(input())
# 1~N번 까지 능력치
S = [list(map(int, input().split())) for _ in range(N)]
selected_nums = [0] * N
INF = 1e9
min_ans = INF


def calc_diff(selected_nums):
    # 스타트팀
    numbers1 = []
    # 링크팀
    numbers2 = []
    # 스타트팀 능력치 합
    ans1 = 0
    # 링크팀 능력치 합
    ans2 = 0
    for n in range(N):
        if selected_nums[n] == 1:
            numbers1.append(n)
        else:
            numbers2.append(n)
    for i in numbers1:
        for j in numbers1:
            ans1 += S[i][j]
    for i in numbers2:
        for j in numbers2:
            ans2 += S[i][j]
    ans = abs(ans1-ans2)
    return ans


def find_min_diff(pre_n, cnt):
    global min_ans
    # 스타트팀, 링크팀이 절반으로 나뉘었을 때
    if cnt == N/2:
        ans = calc_diff(selected_nums)
        if ans < min_ans:
            min_ans = ans
        return
    for n in range(pre_n+1, N):
        selected_nums[n] = 1
        find_min_diff(n, cnt+1)
        selected_nums[n] = 0


find_min_diff(-1, 0)
print(min_ans)
