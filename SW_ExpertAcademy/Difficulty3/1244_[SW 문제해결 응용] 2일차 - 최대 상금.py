def find_interchange(idx):
    # num_list[idx]와 바꿀 인덱스 찾아서 리턴
    # 뒤에서부터 가장 큰 숫자 탐색
    interchange_idx = idx
    for i in range(len(num_list)-1, idx, -1):
        if num_list[interchange_idx] < num_list[i]:
            interchange_idx = i
    
    return interchange_idx

T = int(input())

for test_case in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    num_list = list(map(int, list(num)))

    for idx in range(len(num_list)):
        interchange_idx = find_interchange(idx)
        if interchange_idx != idx:
            num_list[idx], num_list[interchange_idx] = num_list[interchange_idx], num_list[idx]
            cnt -= 1
        if cnt == 0:
            break
    result = ''.join(str(n) for n in num_list)

    print(f'#{test_case} {result}')