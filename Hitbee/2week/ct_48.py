import sys

# def str_to_int(data):
#     return [int(data)]

# input = sys.stdin.readline
# n, m, k = map(int,input().split())
# area = [list(map(str_to_int, input().split())) for _ in range(n)]
# xyds = [list(map(int, input().split())) for _ in range(m)]


# n, m, k = 5, 4, 1
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

# n, m, k = 5, 4, 2
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

# n, m, k = 2, 3 ,8
# area = [[[0], [0]],
#         [[0], [0]]]
# xyds = [[1, 2, 0, 3],
#         [2, 2, 3, 5],
#         [1, 1, 3, 2]]

# 번호, x좌표, y좌표, 방향의 값을 받아 이동
def move(pn, px, py, pa):
    # 북, 동, 남, 서 순으로 이동 범위 지정
    axis = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 이동했다고 가정 해 봄
    mx, my = px+axis[pa][0], py+axis[pa][1]
    # 이동한 위치가 벽이 아니라면
    if (0 <= mx < n) and (0 <= my < n):
        # 이동한 위치 업데이트
        p_axis[pn] = (mx, my)
        # 보고있는 방향 그대로 한칸 이동한 값 return
        return mx, my
    else: # 이동한 위치가 벽이라면
        change_arrow = {0: 2, 1: 3, 2: 0, 3: 1}
        # 이동방향 반대로 바꿈
        cpa = change_arrow[pa]
        # 플레이어가 보고 있는 방향도 반대로 바꿈
        p_arrow[pn] = cpa
        # 이동한 위치 업데이트
        p_axis[pn] = (px+axis[cpa][0], py+axis[cpa][1])
        # 반대 위치로 한칸 이동한 값 return
        return px+axis[cpa][0], py+axis[cpa][1]

# 총 바꾸기
def swap_gun(p, px, py):
    check_gun = len(area[px][py])
    # 총이 없다면
    if check_gun == 0:
        'print("총 없음")'
        return
    'print("총 있음")'
    # 가지고 있는 총보다 바닥에 있는 총들이 더 좋다면
    if p_gun[p] < max(area[px][py]):
        # 만약 총이 있다면
        if p_gun[p] != 0:
            # 내 총 내려놓음
            area[px][py].append(p_gun[p])
        # 총의 공격력이 높은 순서로 정렬
        'print(f"정렬 전: {area[px][py]}")'
        area[px][py] = sorted(area[px][py], reverse=True)
        'print(f"정렬 후: {area[px][py]}")'
        # 가장 공격력 높은 무기가져오면서 자리에 있는 총 제거
        p_gun[p] = area[px][py].pop(0)

# 진사람 강제 이동
def loser_move(loser, bx, by):
    # 싸운 자리에 총 내려놓음
    # if p_gun[loser] != 0: # 들고 있는 총이 있을 때만
    'print("총 있음")'
    area[bx][by].append(p_gun[loser]) # 자리에 내려놓고
    p_gun[loser] = 0 # 진사람 총 없앰
    
    # 진 플레이어가 보고있는 방향
    ba = p_arrow[loser]
    # 플레이어 이동방향으로 강제 이동
    axis = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    'print(f"진 사람이 보고있는 방향: {ba}")'
    'print(p_axis)'
    # 보고있는 위치에서 4방면 전부 확인
    for rotate in range(ba, ba+4):
        # axis 범위를 벗어났을 때 교정
        if rotate > 3:
            rotate = rotate-4
        # 이동했다고 가정 해 봄
        mx, my = bx+axis[rotate][0], by+axis[rotate][1]
        'print(mx, my)'
        # 이동한 위치가 벽이 아니고, 이동한 위치에 플레이어가 없다면
        if (0 <= mx < n) and (0 <= my < n) and (mx, my) not in p_axis.values():
            # 이동한 위치 업데이트
            p_axis[loser] = (mx, my)
            # 보고있는 방향 업데이트
            p_arrow[loser] = rotate
            break
    'print(p_axis)'
    'print("===========")'
    # 이동한 위치에서 총 스왑
    swap_gun(loser, p_axis[loser][0], p_axis[loser][1])

# 싸움 시작
def battle(p1, p2, bx, by):
    p1_power = p_status[p1] + p_gun[p1]
    p2_power = p_status[p2] + p_gun[p2]
    # 승자 패자 플레이어 변수 선언
    win, lose = 0, 0
    if p1_power > p2_power:     # p1이 이겼다면
        win = p1
        lose = p2
    elif p1_power < p2_power:   # p2가 이겼다면
        win = p2
        lose = p1
    else:                       # 비겼다면
        if p_status[p1] > p_status[p2]:
            win = p1
            lose = p2
        else:
            win = p2
            lose = p1
    # 이긴사람 포인트 지급
    'print(f"{win}플레이어가 {p1_power} - {p2_power}만큼 포인트 획득!")'
    p_point[win] += abs(p1_power - p2_power)

    # 진사람
    loser_move(lose, bx, by)

    # 이긴사람
    ## 총 비교해서 바꿈
    swap_gun(win, bx, by)
    ### 이긴사람 위치 업데이트
    p_axis[win] = (bx, by)

# 플레이어 있는지 확인
def check_player(pn, px, py):
    for key, value in p_axis.items():
        # 내 자신은 제외
        if pn == key:
            continue
        
        # 만약 이동한 위치에 플레이어가 있다면
        if value == (px, py):
            'print(f"p1:{pn}, p2:{key} 싸움땅!")'
            battle(pn, key, px, py)
            break
    # 만약 플레이어가 없다면 더 좋은 총으로 바꾸기
    swap_gun(pn, px, py)

# 플레이어들의 변수 설정
p_point = [0] * m   # 포인트
p_status = [0] * m  # 능력치
p_gun = [0] * m     # 총의 공격력
p_arrow = [0] * m   # 이동 방향
p_axis = {}         # 현재 위치

# 초기값 설정
for idx, (x,y,d,s) in enumerate(xyds):
    p_axis[idx] = (x-1, y-1)
    p_arrow[idx] = d
    p_status[idx] = s

for _ in range(k): # k번 만큼 라운드 진행
    '''
    print(f"========{_+1}라운드 시작=============")
    print(p_point)
    print(p_axis)
    '''
    for i in range(m): # 플레이어 순서대로 진행
        dx, dy = move(i, p_axis[i][0], p_axis[i][1], p_arrow[i])

        # 이동한 위치에 플레이어 있는지 확인
        check_player(i, dx, dy)
    '''
    print(p_point)
    print(p_axis)
    print("맵에 있는 총")
    for a in area:
        print(a)
    print("플레이어들이 들고있는 총")
    print(p_gun)
    print(f"========{_+1}라운드 끝=============")
    '''

for p in p_point:
    print(p, end=" ")