import copy

def move_fish(arr, farr, jaws_x, jaws_y):
    for n in range(1, 17):
        if n in farr:
            x, y = farr[n]
            d = arr[x][y][1]
            cnt = 0
            while cnt < 8:
                nx, ny = x+dir[d][0], y+dir[d][1]
                # 이동 가능한 경우
                if 0<=nx<4 and 0<=ny<4 and (nx != jaws_x or ny != jaws_y):
                    if arr[nx][ny]:
                        farr[arr[nx][ny][0]] = (x, y)
                        arr[x][y] = arr[nx][ny]
                    else:
                        arr[x][y] = []
                    farr[n] = (nx, ny)
                    arr[nx][ny] = (n, d)
                    break
                
                d = (d+1)%8
                cnt += 1


def move(arr, farr, x, y, d, cnt):
    global result

    # step 1) 물고기 이동
    move_fish(arr, farr, x, y)
    
    # step 2) 상어 이동
    while 0<=x+dir[d][0]<4 and 0<=y+dir[d][1]<4:
        x += dir[d][0]
        y += dir[d][1]
        if arr[x][y]:  # 물고기가 있는 칸
            tmp_n, tmp_d = arr[x][y]
            narr = copy.deepcopy(arr)
            nfarr = copy.deepcopy(farr)
            del nfarr[tmp_n]
            narr[x][y] = []
            move(narr, nfarr, x, y, tmp_d, cnt+tmp_n)
    
    result = max(result, cnt)
    

if __name__ == '__main__':
    # 입력
    space = []
    fish = dict()  # 물고기 위치 저장
    for i in range(4):
        space.append([])
        arr = list(map(int, input().split()))
        for j in range(0, 8, 2):
            space[i].append((arr[j], arr[j+1]-1)) # 물고기 번호, 방향
            fish[arr[j]] = (i, j//2)

    dir = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
    cnt = 0
    # 상어 (0,0)으로 이동
    jaws_x, jaws_y, jaws_d = 0, 0, space[0][0][1]
    cnt += space[jaws_x][jaws_y][0]
    del fish[space[jaws_x][jaws_y][0]]
    space[jaws_x][jaws_y] = []

    # 출력
    result = 0
    move(space, fish, jaws_x, jaws_y, jaws_d, cnt)
    print(result)