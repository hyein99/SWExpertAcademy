from collections import deque
import copy

def set_wall(cnt):
    global max_safezone

    # step 4) 벽 세개를 새웠으면 안전 구역 구하기
    if cnt == 0:
        nmap = copy.deepcopy(amap)
        safezone = get_safezone(nmap)
        
        # step 6) 안전구역 최대값 구하기
        max_safezone = max(max_safezone, safezone)
        return

    # step 3) 벽 세우기
    for i in range(N):
        for j in range(M):
            if amap[i][j] == 0:
                amap[i][j] = 1
                set_wall(cnt-1)
                amap[i][j] = 0


def get_safezone(arr):
    global origin_safezone
    safezone = origin_safezone - 3

    # step 5) 바이러스 퍼뜨리기
    virus = deque(origin_virus)
    while virus:
        x, y = virus.pop()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    safezone -= 1
                    virus.append((nx, ny))
    
    return safezone


# 입력
N, M = map(int, input().split())
amap = []
origin_safezone = 0    # 안전 영역 개수
for i in range(N):
    amap.append(list(map(int, input().split())))
    origin_safezone += amap[i].count(0)

dir = [(1,0), (-1,0), (0,1), (0,-1)]
max_safezone = 0

# step 1) 바이러스 퍼진 구역 구하기
origin_virus = []
for i in range(N):
    for j in range(M):
        if amap[i][j] == 2:
            origin_virus.append((i,j))

# step 2) 완전 탐색
set_wall(3)

print(max_safezone)