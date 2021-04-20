def make_op(i, result):
    global max_result, min_result

    for j in range(len(op_arr)):
        if i == N:
            max_result = max(max_result, result)
            min_result = min(min_result, result)
            return

        if op_arr[j] > 0:
            op = op_list[j]   # 연산자 설정
            op_arr[j] -= 1    # 연산자 추가 및 연산자 개수 감소
            make_op(i+1, calculate(result, number_arr[i], op))
            op_arr[j] += 1
        

def calculate(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    else:
        if x<0:
            return -(-x//y)
        else:
            return x//y


# 입력
N = int(input())
number_arr = list(map(int, input().split()))
op_arr = list(map(int, input().split())) # +, -, *, %
op_list = ['+', '-', '*', '%']

max_result = -1000000000
min_result = 1000000000
make_op(1, number_arr[0])

print(max_result)
print(min_result)

