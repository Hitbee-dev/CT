import sys, math

input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
store = [list(map(int, input().split())) for _ in range(M)]

# testcase1
# N, M = 5, 3
# area = [[0, 0, 0, 0, 0],
#         [1, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1]]
# store = [[2, 3],
#          [4, 4],
#          [5, 1]]

# testcase2
# N, M = 3, 4
# area = [[0, 0, 1],
#         [1, 1, 0],
#         [1, 1, 0]]
# store = [[2, 3],
#          [1, 1],
#          [3, 3],
#          [1, 2]]

def heuristic(x1, y1, x2, y2):
    return int(math.sqrt(((x2-x1)**2) + ((y2-y1)**2))*10)

def astar(f, g, h, x1, y1, x2, y2):
    # 남 동 서 북
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    buffer = []
    g += 10
    for x, y in zip(dx, dy):
        nx1, ny1 = (x1+x), (y1+y)
        # if -1 == nx1 or N == nx1 or -1 == ny1 or N == ny1:
        #     continue
        # if (nx1, ny1) in wall:
        #     continue
        if (nx1, ny1) in closed_list:
            continue
        h = heuristic(nx1, ny1, x2, y2)
        f = g + h
        buffer.append([f, (nx1, ny1)])
    nx, ny = min(buffer)[1]
    # print(buffer, (nx, ny))
    open_list.append((nx, ny))
    return nx, ny

F, G, H = 0, 0, 0

# basecamp 위치 저장
basecamp = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            basecamp.append([i, j])

# store 위치 재 조정
for idx in range(len(store)):
    sx, sy = store[idx]
    store[idx] = [sx-1, sy-1]

# 가고싶은 편의점에서 가장 가까운 베이스캠프 탐색
## astar 알고리즘을 사용하려면 정확한 출발지점과 도착지점이 있어야 함
wall = []
path_length = [0]*M
for user, (sx, sy) in enumerate(store):
    wall_buffer = []
    for bx, by in basecamp:
        if (sx, sy) in wall:
            continue
        if (bx, by) in wall:
            continue
        open_list = []
        closed_list = []
        nsx, nsy = sx, sy
        open_list.append((nsx, nsy))
        closed_list.append(open_list.pop())
        # print("시작", (nsx, nsy),"목표", (bx, by))
        # astar 알고리즘 실행
        while True:
            nsx, nsy = astar(F, G, H, nsx, nsy, bx, by)
            closed_list.append(open_list.pop())
            if (nsx, nsy) == (bx, by):
                break
        # print("결과", user, open_list, closed_list)

        wall_buffer.append(closed_list)        
    #     print("========================")
    # print("wall buffer",wall_buffer)

    check_path = []
    for wb in wall_buffer:
        if check_path == []:
            check_path = wb
        else:
            if len(check_path) == len(wb): # 최단거리 같을 때
                if check_path[-1][0] == wb[-1][0]: # 행이 같을 때
                    if check_path[-1][1] > wb[-1][1]: # 새 값이 더 작다면
                        check_path = wb # 바꾸기
                else: # 행이 다를 때
                    if check_path[-1][0] > wb[-1][0]: # 새 값이 더 작다면
                        check_path = wb
            elif len(check_path) > len(wb):
                check_path.clear()
                check_path = wb
    # print("최종",check_path, len(check_path))
    wall.append(check_path[0])
    wall.append(check_path[-1])
    path_length[user] = len(check_path)
#     print(wall)
#     print("==========Next Step=========")
# print(path_length)
count = 1
time = 1
while sum(path_length) != len(path_length):
    for i in range(count):
        if path_length[i] > 1:
            path_length[i] -= 1
    if count < M:
        count += 1
    time += 1
    # print(path_length)
    # print(count)
print(time)