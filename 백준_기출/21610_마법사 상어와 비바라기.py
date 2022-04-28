# https://www.acmicpc.net/problem/21610
# 마법사 상어와 비바라기

def get_copycnt(x, y):
    cnt = 0
    # 대각선방향 거리 1(경계를 넘어가면 배제)
    # 물이 있는 바구니수만큼 (r, c)에 물 추가
    for dx, dy in diag_dir:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] > 0:
            cnt += 1
    return cnt


# 입력
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
diag_dir = [(1,1), (1,-1), (-1,-1), (-1,1)]  # 대각선
cloud_arr = [[0]*N for _ in range(N)]  # 구름 유무(1: 유)

# 초기 구름
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for x, y in cloud:
    cloud_arr[x][y] = 1

for _ in range(M):
    d, s = map(int, input().split())
    # 1) 구름 d방향 s칸 이동
    for i in range(len(cloud)):
        x, y = cloud[i]
        nx, ny = (x+(dir[d-1][0])*s)%N, (y+(dir[d-1][1])*s)%N
        cloud_arr[x][y] = 0  # 기존 위치에 있는 구름 사라짐
        cloud[i] = (nx, ny)
        # 2) 구름이 있는 칸에 물+1
        arr[nx][ny] += 1

    # 4) 물복사: cloud에 물 + 1
    for x, y in cloud:
        cloud_arr[x][y] = 1
        arr[x][y] += get_copycnt(x, y)

    cloud = []
    # 5) 물이 2이상인 모든 칸에 구름 생기고 물-2(3에서 구름 사라진 곳 제외)
    for i in range(N):
        for j in range(N):
            if cloud_arr[i][j] == 1:  # 원래 구름있던 자리
                cloud_arr[i][j] = 0
                continue

            if arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud_arr[i][j] = 1
                cloud.append((i, j))

# 출력
result = 0
for i in range(N):
    result += sum(arr[i])
print(result)