T = int(input())

for test_case in range(1, T+1):
    # 입력
    N, K = map(int, input().split())
    grades = []
    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']
    for i in range(1, N+1):
        mid, final, assignment = map(int, input().split())
        sum_grade = mid*0.35+final*0.45+assignment*0.2
        grades.append((i, sum_grade))
        
        if i==K:
            K_grade = sum_grade

    grades.sort(key=lambda x: -x[1])
    idx = grades.index((K, K_grade))   # K의 등수
    cnt_per_grade = len(grades)//10    # 성적당 학생 수
    result = grade_list[idx//cnt_per_grade]

    print(f'#{test_case} {result}')