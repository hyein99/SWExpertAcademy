from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_dict = defaultdict(int)
    arr = list(map(int, input().split()))
    
    max_num = 0
    for a in arr:
        num_dict[a] += 1
        if num_dict[a] > max_num:
            result = a
            max_num = num_dict[a]
        elif num_dict[a] == max_num:
            if a > result:
                result = a

    print(f'#{test_case} {result}')