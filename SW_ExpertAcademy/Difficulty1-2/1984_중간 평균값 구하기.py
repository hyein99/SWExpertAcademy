T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    result = round(sum(arr[1:-1])/8)
                
    print(f'#{test_case} {result}')