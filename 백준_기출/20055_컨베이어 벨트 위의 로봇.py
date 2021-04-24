from collections import deque

# 풀이 2) rotate 사용 > Python3
if __name__ == '__main__':
    # 입력
    N, K = map(int, input().split())
    belt = deque()
    tmp = map(int, input().split())
    for t in tmp:
        belt.append([t, -1]) # (내구도, 올라와있는 로봇 유무(-1은 없다는 의미))
    
    # 변수 선언
    stage = 0            # 단계 진행 번호
    cnt = 0              # 내구도 0인 칸의 개수 카운트

    # 내구도가 0인 칸의 개수가 K 이상인 경우 종료
    while cnt < K:
        stage += 1

        # step 1) 벨트 한칸 회전
        belt.rotate(1)

        # step 2) 가장 먼저 올라간 로봇부터 이동(N-1부터)
        # 1) 내리는 위치에 있는 로봇 내리기
        belt[N-1][1] = -1

        # 2) 이동가능한 로봇 이동하기
        for i in range(N-2, -1, -1):
            if belt[i][1] == 1:
                # 이동하려는 칸에 로봇이 없고, 내구도가 1 이상 남아 있을 경우만 이동 가능
                if belt[i+1][0] > 0 and belt[i+1][1] == -1:
                    belt[i][1] = -1
                    belt[i+1][0] -= 1
                    if i+1 != N-1:  # 이동한 위치가 내리는 곳일 경우 제외
                        belt[i+1][1] = 1
                    if belt[i+1][0] == 0:
                        cnt += 1
         
        # step 3) 올라가는 위치(start)에 로봇 올리기
        if belt[0][0] > 0 and belt[0][1] == -1:
            # belt에 정보 추가하고 내구성 -1
            belt[0][1] = 1
            belt[0][0] -= 1
            if belt[0][0] == 0:
                cnt += 1
        
    print(stage)


# # 풀이 1) 리스트 사용 >> Pypy3
# if __name__ == '__main__':
#     # 입력
#     N, K = map(int, input().split())
#     belt = []
#     tmp = map(int, input().split())
#     for t in tmp:
#         belt.append([t, -1]) # (내구도, 올라와있는 로봇 유무(-1은 없다는 의미))
    
#     # 변수 선언
#     start = 0            # 올라가는 위치 번호
#     stage = 0            # 단계 진행 번호
#     cnt = 0              # 내구도 0인 칸의 개수 카운트
#     NN = 2*N

#     # 내구도가 0인 칸의 개수가 K 이상인 경우 종료
#     while cnt < K:
#         stage += 1

#         # step 1) 벨트 한칸 회전
#         start = (start-1+NN)%NN

#         # step 2) 가장 먼저 올라간 로봇부터 이동(N-1부터)
#         # 1) 내리는 위치에 있는 로봇 내리기
#         down = (start+N-1)%NN
#         belt[down][1] = -1

#         # 2) 이동가능한 로봇 이동하기
#         for i in range(1, N):
#             idx = (down-i+NN)%NN
#             if belt[idx][1] == 1:
#                 # 이동하려는 칸에 로봇이 없고, 내구도가 1 이상 남아 있을 경우만 이동 가능
#                 if belt[(idx+1)%NN][0] > 0 and belt[(idx+1)%NN][1] == -1:
#                     belt[idx][1] = -1
#                     belt[(idx+1)%NN][0] -= 1
#                     if (idx+1)%NN != down:
#                         belt[(idx+1)%NN][1] = 1
#                     if belt[(idx+1)%NN][0] == 0:
#                         cnt += 1
         
#         # step 3) 올라가는 위치(start)에 로봇 올리기
#         if belt[start][0] > 0 and belt[start][1] == -1:
#             # belt에 정보 추가하고 내구성 -1
#             belt[start][1] = 1
#             belt[start][0] -= 1
#             if belt[start][0] == 0:
#                 cnt += 1
        
#     print(stage)