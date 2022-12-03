# 2022/12/1
# 백준 14888번 연산자 끼워넣기

# 숫자 개수
N = int(input())
# N개의 숫자
nums = list(map(int, input().split()))
# 각 연산자 개수 합치면 N-1개
op = list(map(int, input().split()))
used_op = [0] * 4


INF = 1e9
min_ans = INF
max_ans = -INF


# 덧셈, 뺄셈, 곱셈, 나눗셈 계산하는 함수
def calc(i, cnt, ans):
    if i == 0:
        ans += nums[cnt]
    elif i == 1:
        ans -= nums[cnt]
    elif i == 2:
        ans *= nums[cnt]
    elif i == 3:
        if ans < 0:
            ans = -((-ans) // nums[cnt])
        else:
            ans = ans // nums[cnt]
    return ans


def select_operator(cnt, ans):
    global min_ans, max_ans
    if cnt == N-1:
        if ans < min_ans:
            min_ans = ans
        if ans > max_ans:
            max_ans = ans
        return
    for i in range(4):
        if used_op[i] < op[i]:
            used_op[i] += 1
            select_operator(cnt+1, calc(i, cnt+1, ans))
            used_op[i] -= 1


select_operator(0, nums[0])
print(max_ans)
print(min_ans)
