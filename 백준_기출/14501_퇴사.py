# 입력
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

profit = []     # profit[i]: i번째 상담을 했을 때 최대이익
max_profit = 0  # 얻을 수 있는 최대이익
for i in range(len(arr)):
    # step 1) i번째 상담을 했을 때 걸리는 시간과 수익
    time, p = arr[i][0], arr[i][1]

    # step 2) i번째 상담이 N번째 일을 넘어가면 상담할 수 없음
    if i+time > N:
        p = 0

    # step 3) 이전 기록(profit)에 p를 추가하여 최대이익 계산
    np = p
    for j in range(i-1, -1, -1):
        if j + arr[j][0] <= i:   # j번째 상담이 끝나고 새로운 상담을 할 수 있는 기간
            np = max(np, p+profit[j])

    # step 4) profit에 i번째 상담했을때 최대이익 추가 및 전체 최대이익 계산
    max_profit = max(max_profit, np)
    profit.append(np)

print(max_profit)