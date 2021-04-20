def set_team(idx, start, link):
    global min_gap
    
    # 종료 조건
    if idx == N:
        result = abs(calculate_points(start)-calculate_points(link))
        min_gap = min(min_gap, result)
        return

    for j in range(2):
        if j == 0 and len(start)<N//2:
            set_team(idx+1, start+[idx], link)
        elif j == 1 and len(link)<N//2:
            set_team(idx+1, start, link+[idx])

            
def calculate_points(team):
    result = 0
    for t1 in team:
        for t2 in team:
            result += S[t1][t2]
    return result


# 입력
N = int(input())
S = []
min_gap = 0
for i in range(N):
    S.append(list(map(int, input().split())))
    min_gap += sum(S[i])

set_team(0, [], [])

print(min_gap)
