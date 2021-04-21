def dragon_curve(x, y, d, g):
    if g == 0:
        road.append(d)
        nx, ny = x+dir[d][0], y+dir[d][1]
        grid.append((nx, ny))

        return nx, ny
    
    nx, ny = dragon_curve(x, y, d, g-1)
    for r in road[::-1]:
        nd = (r+1)%4
        road.append(nd)
        nx, ny = nx+dir[nd][0], ny+dir[nd][1]
        grid.append((nx, ny))
        
    return nx, ny
    

def count_square(arr):
    result = 0
    for a in arr:
        cnt = 1
        for d in square_dir:
            if (a[0]+d[0], a[1]+d[1]) not in arr:
                cnt = 0
                break
        result += cnt
    return result


# 입력
N = int(input())
grid = []
dir = [(1,0), (0,-1), (-1,0), (0,1)]       # 0(오), 1(위), 2(왼), 3(아래)
for _ in range(N):
    road = []
    x, y, d, g = map(int, input().split()) # 시작점(x,y), 시작방향(d), 세대(g)
    grid.append((x, y))
    dragon_curve(x, y, d, g)

# 출력
square_dir = [(1,0), (1,1), (0,1)]
print(count_square(set(grid)))