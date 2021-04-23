from collections import defaultdict
from collections import deque

def rotate(L):
    # L레벨로 격자 나눔
    for x in range(0, size, L):
        for y in range(0, size, L):
            # 90도 회전
            tmp = []
            for c in range(L):
                for r in range(L-1, -1, -1):
                    tmp.append(board[x+r][y+c])
            cnt = 0
            for r in range(L):
                for c in range(L):
                    board[x+r][y+c] = tmp[cnt]
                    cnt += 1


def reduce_ice():
    reduce_list = []
    for i in range(size):
        for j in range(size):
            if board[i][j] > 0:
                cnt = 0
                for d in dir:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<size and 0<=nj<size and board[ni][nj] > 0:
                        cnt += 1
                if cnt < 3:
                    reduce_list.append((i, j))

    return reduce_list


def bfs(i, j):
    qu = deque()
    qu.append((i, j))
    board[i][j] = -1
    cnt = 0

    while qu:
        x, y = qu.popleft()
        cnt += 1
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<size and 0<=ny<size and board[nx][ny] > 0:
                qu.append((nx, ny))
                board[nx][ny] = -1
    
    return cnt


if __name__ == '__main__':
    # 입력
    N, Q = map(int, input().split())
    board = []
    size = 2**N
    for _ in range(size):
        board.append(list(map(int, input().split())))
    level_list = list(map(int, input().split()))

    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    # Q번 진행
    for q in range(Q):
        L = 2**level_list[q]

        # step 1) L*L크기의 부분격자로 나누어 90도 회전
        rotate(L)
        
        # step 2) 얼음 칸 3개 이상 인접해있지 않은 칸은 얼음의 양 -1
        reduce_list = reduce_ice()
        for x, y in reduce_list:
            board[x][y] -= 1

    # 출력
    # 1) 남아있는 얼음의 합
    total = 0
    for i in range(size):
        total += sum(board[i])
    print(total)
    
    # 2) 가장 큰 덩어리의 크기
    max_size = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] > 0:
                max_size = max(max_size, bfs(i, j))
    print(max_size)

        