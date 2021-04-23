# 풀이 2) itertools combination 사용 >> 520ms
import itertools

def get_chicken_len(chicken):
    # 각 집의 치킨거리를 구해서 도시의 치킨거리를 구하는 함수
    city_chicken_len = 0
    for h in house:
        chicken_len = 100   # N 최대값: 50
        for c in chicken:
            chicken_len = min(chicken_len, abs(h[0]-c[0])+abs(h[1]-c[1]))
        city_chicken_len += chicken_len

    return city_chicken_len


if __name__ == '__main__':
    # 입력
    N, M = map(int, input().split())
    city = []   # 빈칸(0), 집(1), 치킨집(2)
    for _ in range(N):
        city.append(list(map(int, input().split())))
    
    # step 1) 치킨 집(2) 리스트(chicken)와 집(1) 리스트(house) 구하기
    chicken = []
    house = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))

    # step 2) 폐업시키지 않을 치킨집(M)개 조합
    comblist = list(itertools.combinations(chicken, M))
    
    # step 3) 각 조합에 맞는 집의 치킨거리 구하기
    result = 100*N*N
    for comb in comblist:
        result = min(result, get_chicken_len(comb))
    
    # 출력
    print(result)



# 풀이 1) 조합 직접 구현 > 580ms
# def get_chicken_len(chicken):
#     # 각 집의 치킨거리를 구해서 도시의 치킨거리를 구하는 함수
#     city_chicken_len = 0
#     for h in house:
#         chicken_len = 100   # N 최대값: 50
#         for c in chicken:
#             chicken_len = min(chicken_len, abs(h[0]-c[0])+abs(h[1]-c[1]))
#         city_chicken_len += chicken_len

#     return city_chicken_len


# def solution(closed, start):
#     global result
#     # 폐업시킬 치킨집을 완전탐색하는 함수
#     # 조합(치킨집 개수 중 M개 고르기)
#     # closed: 폐업시킬 치킨집
    
#     # 종료조건
#     if len(closed) >= len(chicken) - M:
#         open = set(chicken)-set(closed)
#         result = min(result, get_chicken_len(open))
#         return
    
#     for i in range(start, len(chicken)):
#         closed.append(chicken[i])
#         solution(closed, i+1)
#         closed.pop()


# if __name__ == '__main__':
#     # 입력
#     N, M = map(int, input().split())
#     city = []   # 빈칸(0), 집(1), 치킨집(2)
#     for _ in range(N):
#         city.append(list(map(int, input().split())))
    
#     # step 1) 치킨 집(2) 리스트(chicken)와 집(1) 리스트(house) 구하기
#     chicken = []
#     house = []
#     for i in range(N):
#         for j in range(N):
#             if city[i][j] == 1:
#                 house.append((i, j))
#             elif city[i][j] == 2:
#                 chicken.append((i, j))

#     # 출력
#     result = 100*N*N
#     solution([], 0)
#     print(result)
