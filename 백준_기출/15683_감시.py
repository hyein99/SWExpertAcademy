from collections import deque
import copy

def run_cctv(x, y, arr, dir):
    # (x,y)지점에서 dir 방향으로 감시를 시행한 후 감시된 지역을 구하는 함수
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        while 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] == 6:   # 벽을 만날 경우
                break
            elif arr[nx][ny] == 0: # 빈 공간일 경우
                arr[nx][ny] = -1
            nx, ny = nx+d[0], ny+d[1]
    return arr


def count_empty(arr):
    # 사각지대 개수를 구하는 함수
    empty = 0
    for i in range(N):
        empty += arr[i].count(0)
    return empty


def solution(arr, st):
    # 감시 카메라 작동 경우의 수 완전 탐색하는 함수
    global result

    # 종료조건
    if not st:
        result = min(result, count_empty(arr))
        return

    # cctv 번호에 따라 움직일 수 있는 방향 다르게 설정
    # possible_dir: 움직일 수 있는 방향
    # narr: 참조값 변경 방지
    x, y = st.pop()
    if room[x][y] == 1:
        for k in range(4):
            possible_dir = [dir[k]]
            narr = copy.deepcopy(arr)
            solution(run_cctv(x, y, narr, possible_dir), st)
    elif room[x][y] == 2:
        for k in range(2):
            possible_dir = [dir[k], dir[k+2]]
            narr = copy.deepcopy(arr)
            solution(run_cctv(x, y, narr, possible_dir), st)
    elif room[x][y] == 3:
        for k in range(4):
            possible_dir = [dir[k], dir[(k+1)%4]]
            narr = copy.deepcopy(arr)
            solution(run_cctv(x, y, narr, possible_dir), st)
    elif room[x][y] == 4:
        for k in range(4):
            possible_dir = [dir[k], dir[(k+1)%4], dir[(k+2)%4]]
            narr = copy.deepcopy(arr)
            solution(run_cctv(x, y, narr, possible_dir), st)
    st.append((x, y))


if __name__ == '__main__':
    # 입력
    N, M = map(int, input().split())
    room = []
    for i in range(N):
        room.append(list(map(int, input().split())))
    
    # step 1) cctv 위치를 스택에 저장(st)
    #         5번 cctv의 경우 방향이 확정되기 때문에 따로 저장(cctv)
    st = deque()
    cctv5 = []
    for i in range(N):
        for j in range(M):
            if room[i][j] == 5:
                cctv5.append((i,j))
            elif 1<=room[i][j]<5:
                st.append((i, j))
    
    # step 2) 5번 감시카메라의 감시 영역 확정(-1로 표시)
    dir = [(0,1), (1,0), (0,-1), (-1,0)] # 방향 네 가지
    for x, y in cctv5:
        room = run_cctv(x, y, room, dir)
    
    # 출력
    result = N*M
    solution(room, st)
    print(result)
    
    