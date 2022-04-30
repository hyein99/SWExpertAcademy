# https://www.acmicpc.net/problem/21608
# 상어 초등학교

from collections import defaultdict

def get_want(n1, i, j):
    cnt, empty = 0, 0
    for d in dir:
        ni, nj = i+d[0], j+d[1]
        if 0<=ni<N and 0<=nj<N:
            if seat[ni][nj] == -1:
                empty += 1
                continue
            n2 = seat[ni][nj]
            cnt += want_dir[n1][n2]
    return cnt, empty

# 입력
N = int(input())
seat = [[-1 for _ in range(N)] for _ in range(N)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 인접: 상하좌우
want_dir = dict()
for _ in range(N**2):
    n, s1, s2, s3, s4 = map(int, input().split())
    want_dir[n] = defaultdict(int)
    want_dir[n][s1] = 1
    want_dir[n][s2] = 1
    want_dir[n][s3] = 1
    want_dir[n][s4] = 1  # want_dir[n1][i]: n1이 i를 좋아하는 지 여부

    x, y = 0, 0    # 초기 임시 자리
    max_cnt = 0    # 좋아하는 학생 수 max
    max_empty = 0  # 비어있는 칸 max
    # 자리 탐색
    for i in range(N):
        for j in range(N):
            # 1) 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
            if seat[i][j] == -1:
                cnt, empty = get_want(n, i, j)
                if cnt > max_cnt:
                    x, y = i, j
                    max_cnt = cnt
                    max_empty = empty

                # 2) 여러개면 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로
                elif cnt == max_cnt:
                    if empty > max_empty:
                        x, y = i, j
                        max_empty = empty

                    # 3) 2를 만족하는 칸이 여러개면 행, 열 번호가 작은 칸으로
                    elif empty == max_empty:
                        if seat[x][y] != -1:  # 반례: 0,0
                            x, y = i, j

    # 자리 착석
    seat[x][y] = n

# print(*seat, sep='\n')

# 만족도: 인접한 칸에 좋아하는 학생의 수
satisfied = 0
for i in range(N):
    for j in range(N):
        cnt, empty = get_want(seat[i][j], i, j)
        if cnt > 0:  # 0: 0, 1: 1, 2:10, 3:100, 4:1000
            satisfied += 10**(cnt-1)

print(satisfied)
