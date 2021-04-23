from collections import deque

def bfs(i, j):
    qu = deque()
    qu.append((i, j, 0))
    done = []
    done.append((i, j))
    distance = N*N+1

    fishx, fishy = i, j
    while qu:
        x, y, cnt = qu.popleft()
        if 0 < space[x][y] < size:
            # 종료조건: 더 먼 거리 나오기 시작하면 종료
            if cnt > distance:
                return fishx, fishy, distance

            if cnt < distance:
                distance = cnt
                fishx, fishy = x, y
            else:
                if x < fishx or (x == fishx and y < fishy):
                    distance = cnt
                    fishx, fishy = x, y
        
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<N and 0<=ny<N and space[nx][ny] <= size:
                if (nx, ny) not in done:
                    qu.append((nx, ny, cnt+1))
                    done.append((nx, ny))

    if distance == N*N+1: # 못찾은 경우
        return i, j, -1
    else:
        return fishx, fishy, distance


if __name__ == '__main__':
    # 입력
    N = int(input())
    space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
        for j in range(N):
            if space[i][j] == 9:
                x, y = i, j

    # step 1) 아기상어의 위치(x, y) 0으로 변환
    space[x][y] = 0

    # step 2) 가장 가까운 물고기 위치로 이동
    size = 2
    second = 0
    nx, ny = x, y
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    cnt = 0

    while True:
        nx, ny, distance = bfs(nx, ny)

        # 종료조건(먹을 수 있는 물고기가 없을 때)
        if distance == -1:
            break

        # 이동하여 (nx, ny)에 있는 물고기 먹기
        second += distance
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        space[nx][ny] = 0
        
    # 출력
    print(second)

