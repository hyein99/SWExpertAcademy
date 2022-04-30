# https://www.acmicpc.net/problem/23291
# 어항 정리

from collections import defaultdict

# bfs
def share_fish():
    share_dic = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if fish_arr[i][j] >= 0:
                fish1 = fish_arr[i][j]
                for d in dir:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<N and 0<=nj<N and fish_arr[ni][nj] >= 0:
                        fish2 = fish_arr[ni][nj]
                        # 인접한 두 어항 물고기 수 차이 // 5 = d
                        # d > 0:  물고기가 많은 곳에서 적은 곳으로 d마리 보냄
                        if fish1 > fish2:
                            diff = fish1 - fish2
                            share_dic[(i, j)] -= diff // 5
                            share_dic[(ni, nj)] += diff // 5
                        elif fish1 < fish2:
                            diff = fish2 - fish1
                            share_dic[(i, j)] += diff // 5
                            share_dic[(ni, nj)] -= diff // 5
    # 모든 칸에서 동시 발생
    for (i, j) in share_dic:
        fish_arr[i][j] += share_dic[(i, j)]


def stack_fish1():
    # 가장 왼쪽에 있는 어항을 오른쪽 위에 올려놓음
    fish_arr[0][0], fish_arr[1][1] = fish_arr[1][1], fish_arr[0][0]

    start = 1  # 물고기가 처음 있는 행 번호
    width, height = 1, 1
    while True:
        # 공중부양시킨 어항 중 가장 오른쪽에 있는 어항 아래에 어항 없으면 옮길수 없음
        if N-(start+width) < height+1:
            break

        # 어항들기 (2개 이상 쌓인 어항)
        arr = []
        while fish_arr[start][1] != -1:
            j = 0
            tmp = []
            while fish_arr[start][j] != -1:
                tmp.append(fish_arr[start][j])
                fish_arr[start][j] = -1
                j += 1
            start += 1
            arr.append(tmp)

        # 어항쌓기 (들어서 시계방향 90도 회전)
        height = len(arr[0])
        width = len(arr)
        for i in range(width):
            for j in range(height):
                fish_arr[start+j][width-i] = arr[i][j]


def stack_fish2():
    n = N//4
    for i in range(n):
        fish_arr[i][0], fish_arr[N-i-1][1] = fish_arr[N-i-1][1], fish_arr[i][0]
    for i in range(n, n*2):
        fish_arr[i][0], fish_arr[i+n*2][2] = fish_arr[i+n*2][2], fish_arr[i][0]
    for i in range(n):
        fish_arr[n*2+i][0], fish_arr[N-i-1][3] = fish_arr[N-i-1][3], fish_arr[n*2+i][0]


def make_arow():  # 왼쪽부터, 아래부터
    arr = []
    for i in range(N):
        for j in range(N):
            if fish_arr[i][j] >= 0:
                arr.append(fish_arr[i][j])
                fish_arr[i][j] = -1
    return arr


# 입력
N, K = map(int, input().split())
fish_arr = [[-1 for _ in range(N)] for _ in range(N)]  # fish_arr[0][0]: 제일 왼쪽 아래
row = list(map(int, input().split()))
max_fish, min_fish = max(row), min(row)
for i in range(N):
    fish_arr[i][0] = row[i]

dir = [(1,0), (0,1)]  # 중복으로 안겹치기 위해 두방향만 설정
stage = 0
while max_fish - min_fish > K:  # 최다물고기 - 최소물고기 <= K: 종료
    # 1) 물고기수가 가장 적은 어항에 한 마리 추가(여러개면 다 한 마리씩)
    for i in range(N):
        if fish_arr[i][0] == min_fish:
            fish_arr[i][0] += 1

    # 2) 어항 쌓기
    stack_fish1()

    # 3) 물고기 수 조절
    share_fish()

    # 4) 일렬로 다시 복구
    row = make_arow()
    for i in range(N):
        fish_arr[i][0] = row[i]

    # 5) 어항 쌓기
    stack_fish2()

    # 6) 물고기 수 조절
    share_fish()

    # 7) 일렬로 다시 복구
    row = make_arow()
    for i in range(N):
        fish_arr[i][0] = row[i]

    # 8) min, max 구하기
    max_fish, min_fish = max(row), min(row)

    stage += 1

print(stage)
