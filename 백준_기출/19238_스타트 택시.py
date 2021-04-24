from collections import deque

def find_guest(i, j):
    distance = N*N
    qu = deque()
    qu.append((i, j, 0))
    done = []
    done.append((i, j))

    row, col = i, j
    while qu:
        x, y, cnt = qu.popleft()
        if amap[x][y] > 1:      # 손님 후보
            if cnt < distance:
                distance = cnt
                row, col = x, y
            elif cnt == distance:
                if x < row or (x == row and y < col):
                    row, col = x, y
            else:
                return distance, row, col

        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if (nx, ny) not in done:
                if 0<=nx<N and 0<=ny<N and amap[nx][ny] != 1:
                    qu.append((nx, ny, cnt+1))
                    done.append((nx, ny))
    
    if distance == N*N:
        return -1, i, j
    else:
        return distance, row, col


def get_destination(i, j, guest_num):
    distance = N*N
    qu = deque()
    qu.append((i, j, 0))
    done = []
    done.append((i, j))
    destination_x, destination_y = guest[guest_num]

    while qu:
        x, y, cnt = qu.popleft()
        if x==destination_x and y==destination_y:
            return cnt, destination_x, destination_y

        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if (nx, ny) not in done:
                if 0<=nx<N and 0<=ny<N and amap[nx][ny] != 1:
                    qu.append((nx, ny, cnt+1))
                    done.append((nx, ny))
    
    return -1, destination_x, destination_y


def solution(x, y):
    cnt = M
    while cnt > 0:
        # step 1) 최단거리 손님 찾기(행, 열 참고) + 연료소모 + 손님 위치 0으로
        distance, x, y = find_guest(x, y)
        if distance == -1 or distance > fuel:
            return -1
        fuel -= distance
        guest_num = amap[x][y]
        amap[x][y] = 0

        # step 2) 손님 위치 > 목적지 최단거리 찾기 + 연료소모
        distance, x, y = get_destination(x, y, guest_num)
        if distance == -1 or distance > fuel:
            return -1
        
        # step 3) 목적지에서 연료 두배 충전
        fuel += distance
            
        cnt -= 1

    return fuel


if __name__ == '__main__':
    # 입력
    N, M, fuel = map(int, input().split())   # 크기, 손님 수, 초기연료
    amap = []  # 0(빈칸), 1(벽)
    for _ in range(N):
        amap.append(list(map(int, input().split())))
    R, C = map(int, input().split())  # 운전시작하는 행, 열 번호

    guest = dict()
    for i in range(2, 2+M):           # 손님 번호는 2부터 시작
        startx, starty, endx, endy = map(int, input().split())
        amap[startx-1][starty-1] = i
        guest[i] = (endx-1, endy-1)

    # 출력
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    print(solution(R-1, C-1))
