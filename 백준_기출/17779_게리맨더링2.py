def count_5gu(x, y, d1, d2):
    pop_list = [0]*5

    for i in range(1, N+1):
        for j in range(1, N+1):
            # 5번 선거구 꼭지점((x, y), (x+d1, y-d1), (x+d1+d2, y-d1+d1), (x+d2, y+d2))
            if x<=i<=x+d1+d2 and abs(j-y)<=abs(i-x) and abs(j-(y-d1+d2))<=abs(i-(x+d1+d2)):
                pop_list[4] += population[i][j]
            elif 1<=i<x+d1 and 1<=j<=y:           # 1번 선거구
                pop_list[0] += population[i][j]
            elif 1<=i<=x+d2 and y<j<=N:           # 2번 선거구
                pop_list[1] += population[i][j]
            elif x+d1<=i<=N and 1<=j<y-d1+d2:     # 3번 선거구
                pop_list[2] += population[i][j]
            else:                                 # 4번 선거구
                pop_list[3] += population[i][j]

    # print(*population, sep='\n')
    # print(pop_list)
    # print(max(pop_list), min(pop_list))
    return max(pop_list) - min(pop_list)


# 입력
N = int(input())
population = [[0]*N] # index 1부터 시작하기 위해
for _ in range(N):
    population.append([0]+list(map(int, input().split())))

# 완전 탐색으로 경우의 수 구하는 함수
min_gap = 100*20*20 
for x in range(1, N+1):
    for y in range(2, N+1):  # y >= d1+1
        d1, d2 = 1, 1
        while x+d1+d2<=N and d1<y-1:
            while x+d1+d2<=N and y+d2<=N:
                # print(x, y, d1, d2)
                gap = count_5gu(x, y, d1, d2)
                min_gap = min(min_gap, gap)
                d2 += 1
                # print(gap)
            d1 += 1
            d2 = 1

print(min_gap)
            