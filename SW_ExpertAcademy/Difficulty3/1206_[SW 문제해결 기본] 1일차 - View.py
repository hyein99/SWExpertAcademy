for test_case in range(1, 11):
    length = int(input())
    arr = list(map(int, input().split()))
    check = [-1, -2, 1, 2]
    
    result = 0
    for i in range(len(arr)):
        max_height = 0
        for c in check:
            if 0 <= i+c < len(arr):
                max_height = max(max_height, arr[i+c])
        result += max(0, arr[i]-max_height)

    print(f'#{test_case} {result}')