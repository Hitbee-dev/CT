''' 연산자 끼워넣기
N개의 수로 이루어진 수열 A1 A2 ... AN이 주어진다.
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
연산자는 +, -, *, /으로만 이루어져 있다.
6개의 수로 이루어진 수열이 1 2 3 4 5 6이고,
주어진 연산자가 +2개 -1개 *1개 /1개이면 60가지의 식을 만들 수 있다.
'''
''' Keypoint
1. 식의 계산은 연산자 우선순위를 *무시하고* 앞에서부터 진행해야 한다.
2. 나눗셈은 정수 나눗셈으로 *몫*만 취한다
3. 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
    -> 즉, 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
'''
''' 입력
첫째줄: 수의 개수 N
둘째줄: A1, A2, ... ,AN
셋째줄: 덧셈, 뺄셈, 곱셈, 나눗셈의 개수가 주어짐
'''
''' 출력
첫째줄: 최댓값
둘째줄: 최솟값
'''

# TestCase
'''
N = 6
A = [1, 2, 3, 4, 5, 6]
add, sub, mul, div = [2, 1, 1, 1]
'''

# Solution 1 (Python3 False, PyPy True)
'''
import sys
from itertools import *

# 받아온 숫자를 연산자(문자)로 변경하여 배열에 저장
def operators(op):
    op_str = []
    for idx, op in enumerate(operator):
        if idx == 0: op_str.extend(["+"] * op)
        elif idx == 1: op_str.extend(["-"] * op)
        elif idx == 2: op_str.extend(["*"] * op)
        elif idx == 3: op_str.extend(["/"] * op)
    return op_str

# 계산식
def calc(op, x, y):
    if op == "+": return x+y
    elif op == "-": return x-y
    elif op == "*": return x*y
    elif op == "/":
        if x < 0: return -(abs(x)//y)
        return x//y

input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().split(" ")))
operator = list(map(int, input().split(" ")))
# 연산자의 개수를 연산자 문자로 변환
operator = operators(operator)
min_val = 1e9
max_val = -1e9

# 주어진 연산자로 구현할 수 있는 모든 경우의 수 
for op in list(permutations(operator, len(operator))):
    buf = A[0] # 초기값 설정
    for idx, o in enumerate(op):
        buf = calc(o, buf, A[idx+1])
    max_val = buf if buf > max_val else max_val
    min_val = buf if buf < min_val else min_val
print(max_val)
print(min_val)
'''

# Solution 2
import sys

def dfs(depth, result, add, sub, mul, div):
    global max_val, min_val
    if depth == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return max_val, min_val
    
    if add: # + 먼저 썼을 때
        dfs(depth+1, result+A[depth], add-1, sub, mul, div)
    if sub: # - 먼저 썼을 때
        dfs(depth+1, result-A[depth], add, sub-1, mul, div)
    if mul: # * 먼저 썼을 때
        dfs(depth+1, result*A[depth], add, sub, mul-1, div)
    if div: # / 먼저 썼을 때
        dfs(depth+1, -(abs(result)//A[depth]) if result < 0 else result//A[depth], add, sub, mul, div-1)

input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

dfs(1, A[0], add, sub, mul, div)
print(max_val)
print(min_val)