def move_dust(i, j, d, nums, total, percent):
    global result

    ni, nj = i, j
    for n in nums:
        ni += dir[(d+n)%4][0]
        nj += dir[(d+n)%4][1]

    dust = int(total*percent)
    board[i][j] -= dust
    if 0 <= ni < N and 0 <= nj < N:
        board[ni][nj] += dust
    else:
        result += dust


def spread_dust(i, j, d):
    global result

    # 모래 비율대로 날리기
    i, j = i+dir[d][0], j+dir[d][1]
    total = board[i][j]  # y지점 모래양
    # 1%
    move_dust(i, j, d, [2, 3], total, 0.01)
    move_dust(i, j, d, [1, 2], total, 0.01)
    # 2%
    move_dust(i, j, d, [3, 3], total, 0.02)
    move_dust(i, j, d, [1, 1], total, 0.02)
    # 5%
    move_dust(i, j, d, [0, 0], total, 0.05)
    # 7%
    move_dust(i, j, d, [3], total, 0.07)
    move_dust(i, j, d, [1], total, 0.07)
    # 10%
    move_dust(i, j, d, [0,3], total, 0.1)
    move_dust(i, j, d, [0,1], total, 0.1)

    # 나머지(a)
    ni, nj = i+dir[(d+0)%4][0], j+dir[(d+0)%4][1]
    if 0 <= ni < N and 0 <= nj < N:
        board[ni][nj] += board[i][j]
    else:
        result += board[i][j]
    board[i][j] = 0


if __name__ == '__main__':
    # 입력
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    # 시작점
    x, y = N//2, N//2
    dir = [(0,-1), (1,0), (0,1), (-1,0)]

    result = 0
    cnt, length, length_cnt = 0, 1, 0
    d = 0
    # 종료점
    while x!=0 or y!=0:
        # 모래 흩날리기
        spread_dust(x, y, d)

        x, y = x+dir[d][0], y+dir[d][1]

        cnt += 1
        if cnt == length:
            d = (d+1)%4
            cnt = 0
            length_cnt += 1
        if length_cnt == 2:
            length += 1
            length_cnt = 0

    # 출력
    print(result)