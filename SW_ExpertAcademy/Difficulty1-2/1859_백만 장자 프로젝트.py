T = int(input())

for test_case in range(1, T+1):
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))
    
    arr = arr[::-1]
    result, maxn = 0, 0
    for a in arr:
        if a < maxn:
            result += maxn - a
        elif a > maxn:
            maxn = a

    print(f'#{test_case} {result}')