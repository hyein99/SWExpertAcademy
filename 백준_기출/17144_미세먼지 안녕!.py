def spread_dust():
    # 기존 미세먼지(dust) 상태를 통해 새로운 미세먼지(arr) 상태를 구하기
    arr = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            arr[i][j] += dust[i][j]
            if dust[i][j]>0:  # 미세먼지가 있는 칸(공기청정기 제외)
                cnt = 0       # 확산된 방향 개수
                for d in dir:
                    ni, nj = i+d[0], j+d[1]
                    # 범위 내에 있고 공기청정기가 아닌 칸으로 확산
                    if 0<=ni<R and 0<=nj<C and dust[ni][nj] != -1:
                        arr[ni][nj] += dust[i][j]//5
                        cnt += 1
                arr[i][j] -= dust[i][j]//5*cnt
    return arr


def run_device():
    # 위쪽
    x, y = device_loc[0]
    dir_up = [(0,1), (-1,0), (0,-1), (1,0)]
    circulate(x, y, dir_up)

    # 아래쪽
    x, y = device_loc[1]
    dir_down = [(0,1), (1,0), (0,-1), (-1,0)]
    circulate(x, y, dir_down)


def circulate(x, y, circulate_dir):
    global result

    i = 0
    nx, ny = x, y
    tmp = 0
    while i < 4:
        if 0<=nx+circulate_dir[i][0]<R and 0<=ny+circulate_dir[i][1]<C:
            nx += circulate_dir[i][0]
            ny += circulate_dir[i][1]
            if nx == x and ny == y:
                break
            tmp, dust[nx][ny] = dust[nx][ny], tmp
        else:
            i += 1
    result -= tmp  # 공기청정기가 흡수한 미세먼지


# 입력
R, C, T = map(int, input().split())
dust = []
device_loc = []
result = 2    # 공기청정기
for i in range(R):
    dust.append(list(map(int, input().split())))
    result += sum(dust[i])
    if dust[i][0] == -1:
        device_loc.append((i,0))

# T초동안 미세먼지 확산 + 공기청정기 가동
dir = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(T):
    dust = spread_dust()
    run_device()

# 남은 미세먼지 양 출력
print(result)