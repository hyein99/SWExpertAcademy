def spread_smell():
    for jaw in jaws:
        x, y = jaws[jaw][0], jaws[jaw][1]
        smell_arr[x][y] = [jaw, K]
    

def reduce_smell():
    for i in range(N):
        for j in range(N):
            if smell_arr[i][j]:
                remain_k = smell_arr[i][j][1] - 1
                if remain_k == 0:
                    smell_arr[i][j] = []
                else:
                    smell_arr[i][j][1] = remain_k


def move(jaw):
    # 이동시 우선순위
        # 1) 아무냄새 없는칸
        # 2) 자기 냄새
    x, y, direction = jaws[jaw]
    
    # 우선순위 1
    for d in priority[jaw][direction]:
        nx, ny, nd = x+dir[d][0], y+dir[d][1], d
        if 0<=nx<N and 0<=ny<N:
            if smell_arr[nx][ny] == []:     # 아무냄새 없는칸
                location_arr[x][y] = 0      # 원래 위치에서 jaw 지우기
                jaws[jaw] = [nx, ny, nd]    # 상어 딕셔너리 위치, 방향 정보 수정
                return nx, ny
    
    # 우선순위 2
    for d in priority[jaw][direction]:
        nx, ny, nd = x+dir[d][0], y+dir[d][1], d
        if 0<=nx<N and 0<=ny<N:
            if smell_arr[nx][ny][0] == jaw: # 자기 냄새
                location_arr[x][y] = 0      # 원래 위치에서 jaw 지우기
                jaws[jaw] = [nx, ny, nd]    # 상어 딕셔너리 위치, 방향 정보 수정
                return nx, ny


def solution():
    second = 0
    while len(jaws) > 1:
        second += 1

        # step 1) 모든 상어 이동
        # 한 칸에 여러 상어가 있으면 작은 번호만 남고 다 사라짐
        # 작은 번호 상어 부터 이동하여 이후에 겹치는 상어는 사라짐
        for jaw in range(M):
            if jaw in jaws:
                x, y = move(jaw)
                if location_arr[x][y] != 0:
                    del jaws[jaw]
                else:
                    location_arr[x][y] = jaw+1
        
        # step 2) 냄새 감소
        reduce_smell()

        # step 3) 냄새뿌리기
        spread_smell()
        

        # 종료조건
        if second > 1000:
            return -1
    
    return second


if __name__ == '__main__':
    # 입력
    N, M, K = map(int, input().split()) # 크기, 상어 수(0부터), 지속기간
    location_arr = []  # 상어 위치 배열
    jaws = dict()      # 상어 딕셔너리: 상어 위치 저장(상어 0부터)
    for i in range(N):
        location_arr.append(list(map(int, input().split())))
        for j in range(N):
            if location_arr[i][j] > 0:
                jaws[location_arr[i][j]-1] = [i, j]
    
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    direction_list = list(map(int, input().split())) # 각 상어의 방향(0부터)
    for i in range(M):
        jaws[i].append(direction_list[i]-1)
    
    priority = []  # 각 상어의 이동 우선순위(0부터)
    # ex) priority[a][b][c]: a상어가 b방향일때 c번째 우선순위
    for i in range(M):
        arr = []
        for j in range(4):
            tmp = list(map(int, input().split()))
            for k in range(4):
                tmp[k] -= 1
            arr.append(tmp)
        priority.append(arr)
    
    # 맨처음 모든 상어가 자신의 위치에 냄새 뿌림
    smell_arr = [[[]]*N for _ in range(N)]   # 냄새 배열(상어, 남은기간)
    spread_smell()

    print(solution())