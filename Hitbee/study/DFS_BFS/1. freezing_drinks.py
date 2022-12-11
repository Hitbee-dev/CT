''' 음료수 얼려먹기
N x M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0
칸막이가 존재하는 부분은 1로 표시된다.

구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는것으로 간주

얼음틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

ex) 3개의 아이스크림 생성
4 5
00110
00011
11111
00000
'''

# DFS
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치로도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
n, m = 4, 5
# 2차원 리스트의 맵 정보 입력 받기
graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

for g in graph:
    print(g)

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)
for g in graph:
    print(g)