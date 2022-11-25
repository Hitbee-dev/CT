# 피보나치 수열

'''
피보나치 수열은 아래와 같은 수열이다.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

이를 점화식으로 나타내면 아래와 같다.
a_n = a_{n-1} + a_{n-2}
a_1 = 1
a_2 = 1
'''

def fibo_origin(x):
    if x == 1 or x == 2:
        return 1
    return fibo_origin(x-1) + fibo_origin(x-2)

print(fibo_origin(30))

'''
단, 위 처럼 구현하게 되면 똑같은 값을 계속 계산하기 때문에
수행시간 측면에서 매우 비효율적으로 동작한다.
> fibo(30)은 10억 정도의 연산을 수행한다.
> fibo(35)만 되어도 연산횟수가 비약적으로 증가하는데, 이를 DP로 풀어보자.
'''

'''
Top-Down(하향식) 방식
'''
input_data = 100
# 연산에 필요한 갯수만큼 미리 만들어 놓음
dp = [0] * (input_data+1) # DP Table

def fibo_dp(x):
    if x == 1 or x == 2:
        return 1
    
    # 한 번이라도 계산한적이 있었다면 저장된 값 그대로 반환
    if dp[x] != 0:
        return dp[x]
    
    # 계산한 적 없었다면 값 메모
    dp[x] = fibo_dp(x-1) + fibo_dp(x-2)
    return dp[x]

print(fibo_dp(input_data))
print(dp)

input_data2 = 100
dp2 = [0] * (input_data2+1)

dp2[1], dp2[2] = 1, 1 # 초기 값 설정
for i in range(3, input_data2+1):
    dp2[i] = dp2[i-1] + dp2[i-2]
print(dp2)

'''
결과적으로 3해 5422경 4848조 1792억 6191만 5075라는 값을 얻을 수 있었다.
DP의 최상 활용
'''

