import copy

# 지도에서 지나갈 수 있는 길을 카운트하는 함수
def count_road():
    cnt = 0
    for i in range(N):
        row = amap[i]
        if can_pass(row):
            cnt += 1

        col = [amap[j][i] for j in range(N)]
        if can_pass(col):
            cnt += 1

    return cnt


# 지나갈 수 있는 길인지 판단하는 함수
def can_pass(arr):
    done = []       # 경사로 설치한 곳
    height = arr[0]
    i = 1
    while i < N:
        # 높이가 
        if arr[i] == height:          # 높이가 같으면 패스
            i += 1
            continue

        # 높이가 다르면 경사로를 놓을 수 있는지 확인
        elif arr[i] + 1 == height:     # 내르막길
            for j in range(L):         # 경사로 길이
                # 1) 범위를 벗어나는경우
                # 2) 경사로 바닥의 높이가 일정하지 않을 경우
                # 3) 이미 경사로를 설치한 경우
                if i+j >= N or arr[i+j] != height - 1 or i+j in done:
                    return False
                done.append(i+j)
            height -= 1
            i += L
        
        elif arr[i] - 1 == height:     # 오르막길                 
            for j in range(L):     # 경사로 길이
                if i-j-1 < 0 or arr[i-j-1] != height or i-j-1 in done:
                    return False
                done.append(i-j-1)
            # 오르막길 설치할 땐 경사로 아래쪽끝이 길과 연결되는지 확인 필요
            if i-L-1 >= 0 and i-L-1 not in done and arr[i-L-1] != height:
                return False
            height += 1
            i += 1
        
        else:
            return False
    
    return True


# 입력
N, L = map(int, input().split()) # 지도크기, 경사로 길이
amap = []
for _ in range(N):
    amap.append(list(map(int, input().split())))

result = count_road()

print(result)
