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

# 보고있는 방향으로 이동
def arrow(idx, x, y, num):
    if num == 0: # 북
        if x-1 == -1:
            player_arrow[idx] = 2
            return (x+1, y, 1)
        return (x-1, y, 0)
    elif num == 1: # 동
        if y+1 == n:
            player_arrow[idx] = 3
            return (x, y-1, 1)
        return (x, y+1, 0)
    elif num == 2: # 남
        if x+1 == n:
            player_arrow[idx] = 0
            return (x-1, y, 1)
        return (x+1, y, 0)
    elif num == 3: # 서
        if y-1 == -1:
            player_arrow[idx] = 1
            return (x, y+1, 1)
        return (x, y-1, 0)

def player_power(idx):
    return player_status[idx] + player_gun[idx]

def swap_gun(area_gun, player_gun):
    if player_gun < area_gun:
        area_gun, player_gun = player_gun, area_gun
        return area_gun, player_gun
    return area_gun, player_gun

def rotate(idx, x, y, num):
    # 졌을 때, 가려는 곳에 플레이어가 있거나 벽이라면 90도씩 회전해서 빈 칸이 보이는 순간 이동
    ax, ay, check = arrow(idx, x, y, num)
    if (ax, ay) in player_axis.values() or check == 1:
        for i in range(1, 5):
            if num+i > 3:
                num = (num+i-i)
            else:
                num = num+i
            bx, by, bcheck = arrow(idx, x, y, num)
            if bcheck == 0:
                player_arrow[idx] = num
                return (bx, by, num)
    return (ax, ay, num)
            

# input = sys.stdin.readline
# n, m, k = map(int,input().split())
# # 격자
# area = [list(map(int, input().split())) for _ in range(n)]
# # x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
# xyds = [list(map(int, input().split())) for _ in range(m)]

# n, m, k = 5, 4, 1
# # 격자
# area = [[1, 2, 0, 1, 2],
#         [1, 0, 3, 3, 1],
#         [1, 3, 0, 2, 3],
#         [2, 1, 2, 4, 5],
#         [0, 1, 3, 2, 0]]

# # x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
# xyds = [[1, 3, 2, 3],
#         [2, 2, 1, 5],
#         [3, 3, 2, 2],
#         [5, 1, 3, 4]]

n, m, k = 5, 4, 2
# 격자
area = [[1, 2, 0, 1, 2],
        [1, 0, 3, 3, 1],
        [1, 3, 0, 2, 3],
        [2, 1, 2, 4, 5],
        [0, 1, 3, 2, 0]]
     
# x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
xyds = [[1, 3, 2, 3],
        [2, 2, 1, 5],
        [3, 3, 2, 2],
        [5, 1, 3, 4]]

# n, m, k = 5, 4, 6
# # 격자
# area = [[1, 2, 0, 1, 2],
#         [1, 0, 3, 3, 1],
#         [1, 3, 0, 2, 3],
#         [2, 1, 2, 4, 5],
#         [0, 1, 3, 2, 0]]
     
# # x, y좌표는 둘다 -1씩 해줘야 함(인덱스로 계산하기 편하게)
# xyds = [[1, 3, 2, 3],
#         [2, 2, 1, 5],
#         [3, 3, 2, 2],
#         [5, 1, 3, 4]]

# 플레이어들의 능력치
player_status = [0] * m

# 플레이어가 가지고있는 총의 능력치
player_gun = [0] * m

# 플레이어가 획득한 포인트
player_point = [0] * m

# 플레이어의 이동 방향
player_arrow = [0] * m

# 플레이어들의 초기 위치
player_axis = {}
for idx, (x,y,d,s) in enumerate(xyds):
    player_axis[idx] = (x-1, y-1)
    player_status[idx] = s
    player_arrow[idx] = d

# k라운드동안 반복
for _ in range(k):
    # 4명의 플레이어 한번씩 움직일 수 있도록
    for i in range(m):
        # 플레이어 이동
        dx, dy, _ = arrow(i, player_axis[i][0], player_axis[i][1], player_arrow[i])
        # 이동한 위치에 플레이어 있으면 싸우기
        if (dx, dy) in player_axis.values():
            for key, value in player_axis.items():
                if value == (dx, dy):
                    # 비겼다면
                    if player_power(i) == player_power(key):
                        win = i if player_status[i] > player_status[key] else key
                        lose = i if player_status[i] < player_status[key] else key
                        # 이긴사람한테 포인트 먼저 지급
                        player_point[win] += player_status[win] - player_status[lose]
                    # 바로 이기거나 졌다면
                    else:
                        win = i if player_power(i) > player_power(key) else key
                        lose = i if player_power(i) < player_power(key) else key
                        # 이긴사람한테 포인트 먼저 지급
                        player_point[win] += player_power(win) - player_power(lose)

                    # 졌다면
                    area[dx][dy], player_gun[lose] = swap_gun(area[dx][dy], player_gun[lose])
                    ddx, ddy, _ = rotate(lose, dx, dy, player_arrow[lose])
                    area[ddx][ddy], player_gun[lose] = swap_gun(area[ddx][ddy], player_gun[lose])
                    # 이겼다면
                    area[dx][dy], player_gun[win] = swap_gun(area[dx][dy], player_gun[win])

                    # 플레이어 위치 변경
                    player_axis[win] = (dx, dy)
                    player_axis[lose] = (ddx, ddy)
                    break
        else:
            # 이동한 위치에 플레이어 없으면 총 바꾸고 위치 업데이트
            area[dx][dy], player_gun[i] = swap_gun(area[dx][dy], player_gun[i])
            player_axis[i] = (dx, dy)
        
for p in player_point:
    print(p, end=" ")