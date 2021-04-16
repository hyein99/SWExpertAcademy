T = int(input())

for test_case in range(1, T + 1):
    result = 0    
    arr = list(map(int, input().split()))
    for a in arr:
        result += a if a%2 else 0
    print(f'#{test_case} {result}')