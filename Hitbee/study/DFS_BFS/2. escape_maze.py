''' 미로 탈출
동빈이의 위치는 0, 0이며 N-1, M-1까지 이동해야함
첫 칸도 이동한 칸에 포함됨

입력조건: 첫째줄에 두 정수 N, M이 주어짐
    -> N: 세로(x)길이, M: 가로(y)길이
출력조건: 첫째줄에 최소 이동 칸의 개수를 출력
'''
def dfs(count, x, y):
    # 만약 벽이라면 빠꾸
    if 0 > x or x >= N or 0 > y or y >= M:
        return 
    # 만약 탈출구에 도착했다면
    if x == escape[0] and y == escape[1]:
        for _ in range(N):
            print(maze[_])
        print("=================")  
        print(f"탈출! 이동 횟수: {count}")
        result.append(count)
        return
    # 만약 이동할 수 있는 곳이라면
    if maze[x][y] == 1:
        count = count+1
        maze[x][y] = count
        # 북쪽으로 이동
        dfs(count, x-1, y)
        # 서쪽으로 이동
        dfs(count, x, y-1)
        # 남쪽으로 이동
        dfs(count, x+1, y)
        # 동쪽으로 이동
        dfs(count, x, y+1)

        return
    return


N, M = 5, 6
maze = [[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]

player = [0, 0]
escape = [N-1, M-1]
result = []
dfs(1, player[0], player[1])
print(min(result))