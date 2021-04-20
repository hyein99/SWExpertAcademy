def clean(x, y, d):
    global cnt

    while True:
        # step 1) 현재 위치 청소
        if board[x][y] == 0:
            board[x][y] = 2
            cnt += 1

        # step 2) 현재 방향 기준 왼쪽방향부터 탐색
        dcnt = 4   # dcnt=0이면 네방향 모두 탐색했음을 의미
        while dcnt:
            d = (d + 1)%4    # 왼쪽 방향으로 회전
            leftx, lefty = x + dir[d][0], y + dir[d][1]
            
            # step 2-a) 왼쪽으로 회전하여 step 1)부터 진행
            if board[leftx][lefty] == 0:
                x, y = leftx, lefty
                break
            
            # step 2-b) 왼쪽에 청소할 곳이 없다면, 회전하고 step 2) 반복
            dcnt -= 1
        
        if dcnt==0:  # step 2-a)로 인해 break한 경우 해당하지 않음
            backd = (d + 2)%4
            backx, backy = x + dir[backd][0], y + dir[backd][1]

            # step 2-d) 뒤가 벽이면 탐색 종료
            if board[backx][backy] == 1:
                break
            
            # step 2-d)
            x, y = backx, backy


# 입력
N, M = map(int, input().split())
board = []
x, y, d = map(int, input().split())   # d: 0(북), 1(동), 2(남), 3(서)
for _ in range(N):
    board.append(list(map(int, input().split())))

dir = [(-1,0), (0,-1), (1,0), (0,1)]  # 북쪽부터 반시계방향 순서(북서남동)

if d==1 or d==3:
    d = (d+2)%4  # 북서남동 순서로 맞추기 위해

cnt = 0
clean(x, y, d)
print(cnt)