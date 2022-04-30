# https://www.acmicpc.net/problem/23290
# 마법사 상어와 복제

import copy

def move_fish(x, y, d):
    # 모든 물고기가 한 칸 이동
    cnt = 0
    while cnt < 8:
        nx, ny = x+dir[d][0], y+dir[d][1]
        if 0<=nx<4 and 0<=ny<4:         # 격자 넘어가는 칸
            if nx!=sx or ny!=sy:        # 상어칸
                if smell[nx][ny] == 0:  # 물고기냄새칸
                    return nx, ny, d
        d = (d+7)%8  # 이동할 수 있을 때 까지 45도 반시계 회전
        cnt += 1

    # 이동할 칸이 없으면 이동 x
    return x, y, d


def move_shark(arr, x, y, fish, path):
    # 제외되는 물고기가 가장 많은 방법으로 이동(여러 경우이면 사전순으로 앞서는 방법)
    global max_fish, max_path

    if len(arr) == 3:
        if fish >= max_fish:  # 마지막일수록 사전순서가 높으니까 마지막 값이 남도록 설정
            max_fish = fish   # 최대값 수정
            max_path = path     # 최적경로
        return

    for i in range(4):
        nx, ny = x+sdir[i][0], y+sdir[i][1]
        if 0<=nx<4 and 0<=ny<4:  # 격자 벗어나면 안됨
            new_fish = fish
            if (nx, ny) not in arr:
                new_fish  += len(amap[nx][ny])
            arr.append((nx, ny))
            move_shark(arr, nx, ny, new_fish, path+str(nx)+str(ny))
            arr.pop()


# 입력
M, S = map(int, input().split())  # 물고기수, 마법 연습 횟수
amap = [[[] for _ in range(4)] for _ in range(4)]  # 4*4 격자
for _ in range(M):
    fx, fy, fd = map(int, input().split())
    amap[fx-1][fy-1].append(fd-1)
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1  # 상어 위치

dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
sdir = [(0,1), (1,0), (0,-1), (-1,0)]
smell = [[0]*4 for _ in range(4)]  # 1 이상이면 냄새나는 칸

cnt = 1
while cnt <= S:
    # 1) 상어가 모든 물고기에게 복제 마법 시전(5번에서 복제되어 나타남)
    fcopy = copy.deepcopy(amap)

    # 2) 물고기 이동
    new_map = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if amap[i][j]:
                for k in range(len(amap[i][j])):
                    d = amap[i][j][k]
                    ni, nj, nd = move_fish(i, j, d)
                    new_map[ni][nj].append(nd)
    amap = new_map

    # 3) 상어가 3칸 이동(현재 칸에서 인접한 칸으로 이동 가능)
    max_fish = 0
    max_path = ''
    move_shark([], sx, sy, 0, '')
    for i in range(3):
        sx, sy = int(max_path[2*i]), int(max_path[2*i+1])
        if len(amap[sx][sy]) > 0:  # 물고기가 있는 칸으로 이동하게 되면
            amap[sx][sy] = []      # 그 칸에 있는 모든 물고기는 격자에서 사라지고
            smell[sx][sy] = cnt    # 냄새 남김

    # 4) 두 번 전 연습에서 생긴 물고기 냄새 사라짐
    if cnt > 2:   # 첫번째, 두번째 연습에는 사라질 냄새 없음
        for i in range(4):
            for j in range(4):
                if smell[i][j] == cnt-2:
                    smell[i][j] = 0

    # 5) 물고기 복제
    for i in range(4):
        for j in range(4):
            if fcopy[i][j]:
                amap[i][j].extend(fcopy[i][j])

    cnt += 1


# 출력
result = 0
for i in range(4):
    for j in range(4):
        result += len(amap[i][j])
print(result)