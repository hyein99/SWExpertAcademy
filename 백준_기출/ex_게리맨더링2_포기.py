# 5개의 선거구역

def seperate_gu(x, y, d1, d2):
    for r in range(N):
        for c in range(N):
            if 0<=r<x+d1 and 0<=c<=y:
                gu[r][c] = 1
            elif 0<=r<=x+d2 and y<c<N:
                gu[r][c] = 2
            elif x+d1<=r<N and 0<=c<y-d1+d2:
                gu[r][c] = 3
            elif x+d1<r<N and y-d1+d2<=c<N:
                gu[r][c] = 4
            else:
                gu[r][c] = 5


def get_population():
    for i in range(N):
        for j in range(N):
            g = gu[i][j]
            gu_population[g-1] += pmap[i][j]


# 입력
N = int(input())
pmap = []
for _ in range(N):
    pmap.append(list(map(int, input().split())))

result = 100*20*20

gu = [[0]*N for _ in range(N)]         # 선거구역 나눈 결과
gu_population = [0 for _ in range(N)]  # 각 구의 인구수
seperate_gu(2-1, 4-1, 2, 2)
print(*gu,sep='\n')

# for x in range(1, N-1):
#     for y in range():
#         for d1 in range(1, ):
#             for d2 in range(1, ):
#                 # 1) 구 나누기
#                 gu = [[0]*N for _ in range(N)]         # 선거구역 나눈 결과
#                 gu_population = [0 for _ in range(N)]  # 각 구의 인구수
#                 seperate_gu(x, y, d1, d2)
#
#                 # 2) 각 구 의 인구수 구하기
#                 get_population()
#
#                 # 3) 최대 선거구-최소 선거구 차이 구하기
#                 diff = max(gu_population) - min(gu_population)
#                 result = min(result, diff)
#
# print(result)