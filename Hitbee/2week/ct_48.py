''' 싸움땅
게임은 n * n 크기의 격자에서 진행됨
각 격자에는 무기들이 있을 수 있음
초기에는 무기들이 없는 빈 격자에 플레이어들이 위치하고, 초기능력치를 가짐
각 플레이어의 초기 능력치는 모두 다름

첫번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동함.
-> 만약 해당 방향으로 이동할 때 격자를 벗어나면 반대 방향으로 1만큼 이동

만약 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인
자리에 총이 있으면 플레이어는 총을 획득하는데, 이미 총을 가지고 있다면 더 공격력이 쎈걸 가져가고, 들고있던는 그 자리에 둠

이동한 방향에 플레이어가 있다면 두 플레이어가 싸움
해당 플레이어의 초기 능력치와, 가지고 있는 총의 공격력을 비교해서 더 큰 플레이어가 이김
-> 만약 둘의 수치가 같다면 플레이어의 초기 능력치가 높은 사람이 이김

이긴 플레이어는 각 플레이어의 초기 능력치와, 가지고 있는 총의 공격력의 합의 차이만큼 포인트를 획득

진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동함.
-> 만약 원래 이동하려던 칸에 다른 플레이어가 있거나 벽이라면 오른쪽으로 90도 회전
-> 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려놓음

이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고,
나머지 총들은 해당 격자에 내려놓음

위 과정을 1~n번 플레이어까지 순차적으로 한번 진행하면 1라운드가 끝남

k라운드 동안 게임을 진행하면서 각 플레이어들이 획득한 포인트를 출력하는 프로그램을 작성하시오.

첫번째 줄에 n, m, k가 공백을 기준으로 주어짐
n = 격자의 크기
m = 플레이어의 수
k = 라운드의 수

2번째 줄 부터 n개의 줄에 걸쳐 격자에 있는 총의 정보가 주어짐

이후 m개의 줄에 걸쳐 플레이어들의 정보 x, y, d, s가 공백을 사이에 두고 주어짐
x, y = 플레이어의 위치
d = 방향
s = 초기능력치

방향 d는 0, 1, 2, 3
         위 오 아 왼
'''

import sys

# def str_to_int(data):
#     return [int(data)]

# input = sys.stdin.readline
# n, m, k = map(int,input().split())
# area = [list(map(str_to_int, input().split())) for _ in range(n)]
# xyds = [list(map(int, input().split())) for _ in range(m)]

'''
n, m, k = 5, 4, 1
# 격자
area = [[[1], [2], [0], [1], [2]],
        [[1], [0], [3], [3], [1]],
        [[1], [3], [0], [2], [3]],
        [[2], [1], [2], [4], [5]],
        [[0], [1], [3], [2], [0]]]

# x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
xyds = [[1, 3, 2, 3],
        [2, 2, 1, 5],
        [3, 3, 2, 2],
        [5, 1, 3, 4]]

n, m, k = 5, 4, 2
# 격자
area = [[[1], [2], [0], [1], [2]],
        [[1], [0], [3], [3], [1]],
        [[1], [3], [0], [2], [3]],
        [[2], [1], [2], [4], [5]],
        [[0], [1], [3], [2], [0]]]
     
# x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
xyds = [[1, 3, 2, 3],
        [2, 2, 1, 5],
        [3, 3, 2, 2],
        [5, 1, 3, 4]]
'''
# n, m, k = 5, 4, 6
# # 격자
# area = [[[1], [2], [0], [1], [2]],
#         [[1], [0], [3], [3], [1]],
#         [[1], [3], [0], [2], [3]],
#         [[2], [1], [2], [4], [5]],
#         [[0], [1], [3], [2], [0]]]
     
# # x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
# xyds = [[1, 3, 2, 3],
#         [2, 2, 1, 5],
#         [3, 3, 2, 2],
#         [5, 1, 3, 4]]

n, m, k = 3, 5, 1
area = [[[0], [5], [0]],
        [[0], [0], [4]],
        [[5], [3], [0]]]
xyds = [[1, 1, 0, 2],
        [3, 3, 2, 1],
        [1, 3, 2, 5],
        [2, 1, 1, 3],
        [2, 2, 1, 4]]

def move(idx, x, y, d):
    global p_move
    arrow = [(-1, 0),(0, 1),(1, 0),(0, -1)]
    # 그냥 이동 가능하다면 이동한 방향 return
    if (-1 < x+arrow[d][0] < n) and (-1 < y+arrow[d][1] < n):
        return x+arrow[d][0], y+arrow[d][1]
    # 벽이라 이동 못하면 방향 전환 + 반대로 이동
    change_move = {0: 2, 1: 3, 2: 0, 3: 1}
    d = change_move[d]
    p_move[idx] = d
    return x+arrow[d][0], y+arrow[d][1]

# 여기 문제가 있는게 확실하다;;
def lose_move(idx, x, y, d):
    global p_move
    arrow = [(-1, 0),(0, 1),(1, 0),(0, -1)]
    # 벽이나 플레이어 때문에 이동 못하면 90도 방향 전환 + 전환한 방향으로 이동
    for index in range(d, d+4):
        if index > 3:
            index = index-4
        p_move[idx] = index
        
        # print(f"이동방향:{index}")
        # 벽, 플레이어 등 간섭 없이 이동 가능하다면 이동한 방향 return
        if (-1 < x+arrow[index][0] < n) and (-1 < y+arrow[index][1] < n) and (x+arrow[index][0], y+arrow[index][1]) not in p_loc.values():
            fx, fy = x+arrow[index][0], y+arrow[index][1]
            # print(f"{idx}플레이어 방향은{index}, 위치는 {fx, fy}로 쫒겨남")
            # 위치 업데이트
            p_loc[idx] = (fx, fy)
            # 이동한 위치에서 총 바꿈
            area[fx][fy], p_gun[lose] = swap_gun(area[fx][fy], p_gun[lose])
            break

def swap_gun(guns, mygun):
    guns = sorted(guns, reverse=True)
    if max(guns) > mygun:
        buf_gun = mygun
        mygun = guns.pop(0)
        guns.append(buf_gun)
        return guns, mygun
    return guns, mygun

def p_power(ps, pg):
    return ps+pg

# 플레이어들의 현재 위치
p_loc = {}

# 플레이어들이 보고 있는 방향
p_move = [0] * m

# 플레이어들의 능력치
p_status = [0] * m

# 플레이어들의 총
p_gun = [0] * m

# 플레이어들의 포인트
p_point = [0] * m

# 플레이어들의 초기값 설정
for idx , (x,y,d,s) in enumerate(xyds):
    p_loc[idx] = (x-1, y-1)
    p_move[idx] = d
    p_status[idx] = s

# k번 만큼 라운드 진행
for _ in range(k):
    # 플레이어 순서대로 본인이 향하는 방향으로 이동
    for i in range(m):
        dx, dy = move(i, p_loc[i][0], p_loc[i][1], p_move[i])

        # 만약 이동하려는 위치에 플레이어가 없다면
        if (dx, dy) not in p_loc.values():
            area[dx][dy], p_gun[i] = swap_gun(area[dx][dy], p_gun[i])
            p_loc[i] = (dx, dy)
        else: # 이동하려는 위치에 플레이어가 있다면
            # 싸움땅!
            for key, value in p_loc.items():
                # 본인제외
                if key == i:
                    continue
                # 만약 몇번째 플레이어랑 마추졌는지 찾았다면
                if value == (dx, dy):
                    p1 = p_power(p_status[i], p_gun[i])
                    p2 = p_power(p_status[key], p_gun[key])
                    # print(f"p1: {p1}, p2: {p2}")
                    # 비겼다면 플레이어 능력치 순으로 승자 패자 가림
                    if p1 == p2:
                        win = i if p_status[i] > p_status[key] else key
                        lose = i if p_status[i] < p_status[key] else key
                        # print(f"win: {win}, lose: {lose}")
                    else: # 비긴게 아니라 한번에 결과가 나왔으면 승자 패자 가림
                        win = i if p1 > p2 else key
                        lose = i if p1 < p2 else key
                    # 이긴사람한테 포인트 줌
                    p_point[win] += abs(p1 - p2)
                    p_loc[win] = (dx, dy)
                    # 진사람
                    # 총 내려놓음
                    area[dx][dy].append(p_gun[lose])
                    p_gun[lose] = 0
                    # 1칸 이동(플레이어나 벽 없으면 그대로, 있으면 90도씩 회전)
                    lose_move(lose, dx, dy, p_move[lose])

                    # 이긴사람
                    area[dx][dy], p_gun[win] = swap_gun(area[dx][dy], p_gun[win])
        # for idx, (s, g) in enumerate(zip(p_status, p_gun)):
        #     print(idx, (s, g), end = " ")

for p in p_point:
    print(p, end=" ")