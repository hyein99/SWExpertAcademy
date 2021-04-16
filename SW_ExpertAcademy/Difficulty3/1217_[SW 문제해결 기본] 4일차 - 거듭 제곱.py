def multiply(n, m):
    if m == 0:
        return 1
    return n*multiply(n, m-1)

for _ in range(10):
    test_case = int(input())
    result = 0
    N, M = map(int, input().split())
    result = multiply(N, M)

    print(f'#{test_case} {result}')