def put_block(arr, t, y):
    if t == 1:
        for i in range(2, 6):
            if arr[i][y] == 1:
                arr[i-1][y] = 1
                return
        arr[5][y] = 1
        return

    elif t == 2:
        for i in range(2, 6):
            if arr[i][y] == 1 or arr[i][y+1] == 1:
                arr[i-1][y] = 1
                arr[i-1][y+1] = 1
                return
        arr[5][y] = 1
        arr[5][y+1] = 1
        return

    else:
        for i in range(2, 6):
            if arr[i][y] == 1:
                arr[i-1][y] = 1
                arr[i-2][y] = 1
                return
        arr[5][y] = 1
        arr[4][y] = 1
        return


if __name__ == '__main__':
    N = int(input())
    green = [[0]*4 for _ in range(6)]
    blue = [[0]*4 for _ in range(6)]
    # 블루는 행열 변환?

    grade = 0
    for _ in range(N):
        # 3종류 블록에 따라 블록 놓기
        t, x, y = map(int, input().split())
        put_block(green, t, y)
        if t == 1:
            put_block(blue, 1, 3-x)
        elif t == 2:
            put_block(blue, 3, 3-x)
        else:
            put_block(blue, 2, 2-x)
        

        # 삭제할 행/열이 있는지 확인
        for i in range(6):
            if sum(green[i]) == 4:
                green = [[0]*4]+green[:i]+green[i+1:]
                grade += 1
            if sum(blue[i]) == 4:
                blue = [[0]*4]+blue[:i]+blue[i+1:]
                grade += 1
    
        # 연한색(0,1)행 만나면 전체가 내려감
        gcnt, bcnt = 0, 0
        for i in range(2):
            if sum(green[i]) > 0:
                gcnt += 1
            if sum(blue[i]) > 0:
                bcnt += 1
        if gcnt:
            green = [[0]*4 for _ in range(gcnt)] + green[:-gcnt]
        if bcnt:
            blue = [[0]*4 for _ in range(bcnt)] + blue[:-bcnt]

    # 출력
    # 점수
    print(grade)
    # 초록색 파란색 보드에 있는 칸의 개수
    result = 0
    for i in range(6):
        result += sum(green[i])+sum(blue[i])
    print(result)
    