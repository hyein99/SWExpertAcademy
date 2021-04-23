# 풀이 2) 파이썬 936ms
def count_5gu(x, y, d1, d2):
    # step 0) 5구역을 표시하기 위한 리스트(tmp)와 각구의 인구수를 나타낼 리스트(pop_list) 생성
    tmp = [[0]*(N+1) for _ in range(N+1)]
    pop_list = [0]*5

    # step 1) 5번 선거구 경계선 표시
    tmp[x][y] = 5
    for i in range(1, d1+1):
        tmp[x+i][y-i] = 5
    for i in range(1, d2+1):
        tmp[x+i][y+i] = 5
    for i in range(1, d2+1):
        tmp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        tmp[x+d2+i][y+d2-i] = 5

    # step 2) 1번~4번 선거구 인구수 구하기
    # 1번
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if tmp[i][j] == 5:
                break
            pop_list[0] += population[i][j]

    # 2번
    for i in range(1, x+d2+1):
        for j in range(N, y, -1):
            if tmp[i][j] == 5:
                break
            pop_list[1] += population[i][j]

    # 3번
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2):
            if tmp[i][j] == 5:
                break
            pop_list[2] += population[i][j]
    
    # 4번
    for i in range(x+d2+1, N+1):
        for j in range(N, y-d1+d2-1, -1):
            if tmp[i][j] == 5:
                break
            pop_list[3] += population[i][j]
    
    pop_list[4] = total - sum(pop_list)

    return max(pop_list) - min(pop_list)


if __name__ == '__main__':
    # 입력
    N = int(input())
    population = [[0]*N] # index 1부터 시작하기 위해
    total = 0
    for i in range(N):
        population.append([0]+list(map(int, input().split())))
        total += sum(population[i+1])

    # 완전 탐색으로 경우의 수 구하기
    min_gap = 100*20*20
    for x in range(1, N+1):
        for y in range(1, N+1):
            for d1 in range(1, N+1):
                for d2 in range(1, N+1):
                    if x+d1+d2>N or y-d1<1 or y+d2>N:
                        continue
                    min_gap = min(min_gap, count_5gu(x, y, d1, d2))

    print(min_gap)
            


# 풀이 1) 파이썬 1924ms
# def count_5gu(x, y, d1, d2):
#     pop_list = [0]*5

#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             # 5번 선거구 꼭지점((x, y), (x+d1, y-d1), (x+d1+d2, y-d1+d1), (x+d2, y+d2))
#             if x<=i<=x+d1+d2 and abs(j-y)<=abs(i-x) and abs(j-(y-d1+d2))<=abs(i-(x+d1+d2)):
#                 pop_list[4] += population[i][j]
#             elif 1<=i<x+d1 and 1<=j<=y:           # 1번 선거구
#                 pop_list[0] += population[i][j]
#             elif 1<=i<=x+d2 and y<j<=N:           # 2번 선거구
#                 pop_list[1] += population[i][j]
#             elif x+d1<=i<=N and 1<=j<y-d1+d2:     # 3번 선거구
#                 pop_list[2] += population[i][j]
#             else:                                 # 4번 선거구
#                 pop_list[3] += population[i][j]

#     return max(pop_list) - min(pop_list)


# # 입력
# N = int(input())
# population = [[0]*N] # index 1부터 시작하기 위해
# for _ in range(N):
#     population.append([0]+list(map(int, input().split())))

# # 완전 탐색으로 경우의 수 구하는 함수
# min_gap = 100*20*20 
# for x in range(1, N+1):
#     for y in range(2, N+1):  # y >= d1+1
#         d1, d2 = 1, 1
#         while x+d1+d2<=N and d1<y-1:
#             while x+d1+d2<=N and y+d2<=N:
#                 gap = count_5gu(x, y, d1, d2)
#                 min_gap = min(min_gap, gap)
#                 d2 += 1
#             d1 += 1
#             d2 = 1

# print(min_gap)
            