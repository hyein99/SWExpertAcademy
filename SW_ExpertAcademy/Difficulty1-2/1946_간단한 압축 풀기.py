T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    length = 10
    result = ''
    for _ in range(N):
        char, num = input().split()
        num = int(num)
        while num:
            if num < length:
                result += char*num
                length -= num
                num = 0
            else:
                result += char*length+'\n'
                num -= length
                length = 10
                
    print(f'#{test_case}')
    print(result)