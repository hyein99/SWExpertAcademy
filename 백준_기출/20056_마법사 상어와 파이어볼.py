def move():
    for f in fireball:
        r, c, m, s, d = fireball[f]
        nr, nc = (r+(dir[d][0])*s+N)%N, (c+(dir[d][1])*s+N)%N
        # 보드 이동
        board[r][c].remove(f)
        board[nr][nc].append(f)
        # 파이어볼 정보 수정
        fireball[f] = [nr, nc, m, s, d]


def merge_and_seperate(x, y):
    global last_f

    new_m, new_s, new_d = 0, 0, 0
    for f in board[x][y]:
        r, c, m, s, d = fireball[f]
        new_m += m
        new_s += s
        new_d += d%2
        # 방향 홀수 짝수 구하기
        del fireball[f]  # fireball dict에서 지우기
    
    # 새로 생성될 파이어볼의 질량, 속도, 방향 구하기
    new_m //= 5
    new_s //= len(board[x][y])
    if new_d == 0 or new_d == len(board[x][y]):
        new_d = 0
    else:
        new_d = 1

    # board에서 기존 파이어볼 지우기
    board[x][y] = []

    # 4개로 나누기
    if new_m == 0:  # 질량이 0인 파이어볼 소멸
        return
    for i in range(last_f+1, last_f+5):
        fireball[i] = [x, y, new_m, new_s, new_d]
        board[x][y].append(i)
        new_d += 2
    
    # 마지막 파이어볼 번호 갱신
    last_f += 4


if __name__ == '__main__':
    # 입력
    N, M, K = map(int, input().split()) # 격자 크기, 파이어볼 개수, 명령 횟수
    board = [[[] for _ in range(N)] for _ in range(N)]
    fireball = dict()   # 번호 1부터 시작
    for i in range(1, M+1):
        r, c, m, s, d = map(int, input().split())
        board[r-1][c-1].append(i)
        fireball[i] = (r-1, c-1, m, s, d)

    last_f = M
    dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    for _ in range(K):
        # step 1) 파이어볼 이동
        move()

        # step 2) 이동 후 2개 이상 파이어볼이 있는 칸
        for i in range(N):
            for j in range(N):
                if len(board[i][j]) >= 2:
                    merge_and_seperate(i, j)

    # step 3) 질량 합 구하기
    result = 0
    for f in fireball:
        result += fireball[f][2]
    print(result)
        