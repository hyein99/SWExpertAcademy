# https://www.acmicpc.net/problem/23288
# 주사위 굴리기2

from collections import deque

def roll_dice(d):
    if d == '동':
        tmp = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    elif d == '남':
        tmp = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    elif d == '서':
        tmp = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    else:  # 북
        tmp = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]

    for i in range(6):
        dice[i] = tmp[i]


# bfs
def count_moveable(i, j, n):
    cnt = 1
    qu = deque()
    qu.append((i, j))
    done = [(i, j)]

    while qu:
        x, y = qu.popleft()
        for d in dir:                 # 방향탐색
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<M:
                if (nx, ny) in done:  # 방문여부 확인
                    continue
                done.append((nx, ny))

                if amap[nx][ny] == n:
                    cnt += 1
                    qu.append((nx, ny))

    return cnt


# 입력
N, M, K = map(int, input().split())
amap = []
for _ in range(N):
    amap.append(list(map(int, input().split())))

dice = [1, 4, 2, 3, 5, 6]  # 윗면, 왼, 위, 오, 아래, 아랫면
dice_dir = ['동', '남', '서', '북']
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 동남서북
result = 0    # 점수 합
x, y = 0, 0   # 처음 위치
d = 0         # 처음 이동방향: 동쪽
while K > 0:
    # 1) 주사위가 이동 방향으로 한칸 굴러감
    nx, ny = x+dir[d][0], y+dir[d][1]
    if 0<=nx<N and 0<=ny<M:
        x, y = nx, ny
    else:  # 칸이 없으면 이동방향 반대로, 한칸
        d = (d+2)%4
        x, y = x+dir[d][0], y+dir[d][1]

    roll_dice(dice_dir[d])
    bottom = 7-dice[0]  # dice[0]: 윗면

    # 2) 도착 칸 점수 획득: 칸에 있는 숫자 * 동서남북 방향에 이동할 수 있는 칸 수(같은 숫자)
    result += amap[x][y] * count_moveable(x, y, amap[x][y])

    # 3) 방향 결정(주사위 아랫면: A, 칸: B)
    if bottom > amap[x][y]:   # A > B: 90도 시계방향 회전
        d = (d+1)%4
    elif bottom < amap[x][y]: # A < B: 90도 반시계
        d = (d+3)%4
    # A = B: 이동방향 그대로

    K-= 1

print(result)