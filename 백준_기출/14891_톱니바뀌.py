def move_gear(num, direction):
    # step 1) 같이 회전시킬 톱니 구하기
    i, j = num, num
    move_list = [num]
    # 왼쪽
    while i>=0:
        if i - 1 >= 0:
            if gear[i][(top[i]+6)%8] != gear[i-1][(top[i-1]+2)%8]:
                # print(f'i:{i}, ')
                move_list.append(i-1)
            else:
                break
        i -= 1

    # 오른쪽
    while j<4:
        if j + 1 < 4:
            if gear[j][(top[j]+2)%8] != gear[j+1][(top[j+1]+6)%8]:
                move_list.append(j+1)
            else:
                break
        j += 1
    
    # step 2) 회전
    for m in move_list:
        # direction: 1(시계), -1(반시계)
        if abs(m-num)%2 == 0: # num이 도는 방향(direction)과 같은 방향으로 회전
            top[m] = (top[m] - direction + 8)%8
        else:
            top[m] = (top[m] + direction + 8)%8


def get_score():
    result = 0
    for i in range(4):
        # N: 0, S: 1
        if gear[i][top[i]] == 1:
            result += point[i]

    return result


# 입력
gear = []
for _ in range(4):
    gear.append(list(map(int, list(input()))))
K = int(input())
top = [0]*4  # 현재 12시방향에 있는 문자의 순서
for _ in range(K):
    num, direction = map(int, input().split())
    move_gear(num-1, direction)

# 점수 계산
point = [1,2,4,8]
print(get_score())
