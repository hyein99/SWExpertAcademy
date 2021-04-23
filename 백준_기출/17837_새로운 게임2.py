def change_direction(k):
    if k == 0:
        return 1
    elif k == 1:
        return 0
    elif k == 2:
        return 3
    else:
        return 2


def move(k):
    # step 1) 현재 위치 구하기
    (x, y), d = location[k]

    # step 2) k와 함께 움직일 말 구하고 원래 위치에서 제거
    move_list = [] # 위에서부터
    idx = 0
    while board[x][y][idx] != k:
        move_list.append(board[x][y][idx])
        idx += 1
    move_list.append(k)
    if len(board[x][y]) == 1:
        board[x][y] = []
    else:
        board[x][y] = board[x][y][idx+1:]
    
    # step 3) 이동할 칸 구하여 board[nx][ny]에 move_list 추가
    nx, ny = x+dir[d][0], y+dir[d][1]
    # case1) 체스판을 벗어나는 경우
    if nx<0 or nx>=N or ny<0 or ny>=N:
        d = change_direction(d)
        nx, ny = x+dir[d][0], y+dir[d][1]
        # case1-1) 방향 돌렸는데 파란색인 경우
        if color_board[nx][ny] == 2:
            nx, ny = x, y
            board[nx][ny] = move_list + board[nx][ny]
    # case2) 파란색인 경우
    elif 0<=nx<N and 0<=ny<N and color_board[nx][ny] == 2:
        d = change_direction(d)
        nx, ny = x+dir[d][0], y+dir[d][1]
        # case2-1) 방향 돌렸는데 파란색이거나 벗어나는 경우
        if (nx<0 or nx>=N or ny<0 or ny>=N) or color_board[nx][ny] == 2:
            nx, ny = x, y
            board[nx][ny] = move_list + board[nx][ny]

    # case3) 방향을 바꿔서 흰or빨 이거나 처음부터 흰or빨 인경우
    if x != nx or y != ny:
        # case3-1) 흰색인 경우
        if color_board[nx][ny] == 0:
            board[nx][ny] = move_list + board[nx][ny]
        # case3-2) 빨간색인 경우
        elif color_board[nx][ny] == 1:
            board[nx][ny] = move_list[::-1] + board[nx][ny]
    
    # step 4) move_list에 있는 말들 location 바꾸기
    for m in move_list[:-1]:
        location[m] = ((nx, ny), location[m][1])
    location[k] = ((nx, ny), d)

    return nx, ny


def play():
    stage = 1
    while stage <= 1000: # 종료조건1
        # K개의 말 이동하기
        for i in range(K):
            x, y = move(i)

            # 종료조건2
            # 말이 4개 이상 쌓일 경우
            if len(board[x][y]) >= 4:
                return stage

        stage += 1

    return -1


if __name__ == '__main__':
    # 입력
    N, K = map(int, input().split()) # 체스판 크기, 말의 개수
    color_board = []                 # 흰색(0), 빨간색(1), 파란색(2)
    for _ in range(N):
        color_board.append(list(map(int, input().split())))

    dir = [(0,1), (0,-1), (-1,0), (1,0)]
    board =[[[]]*N for _ in range(N)]  # board[i][j]: (i,j)에 있는 말
    location = dict()                  # location[i]: i번째 말의 위치와 방향
    for i in range(K):
        x, y, d = map(int, input().split())
        location[i] = ((x-1,y-1), d-1)
        if not board[x-1][y-1]:
            board[x-1][y-1] = [i]
        else:
            board[x-1][y-1].append(i)

    # 출력
    print(play())
