# def check_location(location, destination, color, num1):
#     for i in range(4):
#         c = location[i][1]
#         d = location[i][0]
#         # 색도 같고 위치도 같은 경우
#         if c == color and d == destination:
#             return False
        
#         # 10/20/30/25/40에 겹치는 경우
#         if num1%5 == 0:
#             if c == 0:
#                 num2 = d*2
#             elif c == 1:
#                 num2 = blue1[d]
#             elif c == 1:
#                 num2 = blue2[d]
#             else:
#                 num2 = blue3[d]

#             if num1 == 30 and num2 == 30:
#                 if c>0 and color>0:
#                     return False
#             elif num1 ==  num2:
#                 return False

#     return True


# def check_color(x):
#     if x == 5:
#         return 1
#     elif x  == 10:
#         return 2
#     elif x == 15:
#         return 3
#     else:
#         return 0


# def solution(idx, location, grade):
#     global result

#     # 종료조건
#     if idx == 10:
#         # 최대점수 계산
#         result = max(result, grade)
#         return

#     for i in range(4):
#         x, color = location[i]
#         new_grade = grade
#         if x == -1:    # 이미 도착한 말은 패스(나간 말은 -1로 저장)
#             continue
#         else:
#             if color == 0:
#                 new_x = x+dice[idx]
#                 # i번째 주사위를 던져 도착한 경우
#                 if new_x > 20:
#                     location[i][0] = -1
#                 else:
#                     # 가려고 하는 위치에 다른 말이 있는지 확인
#                     if not check_location(location, new_x, color, 2*new_x):
#                         continue
#                     # 가려고 하는 위치의 색 확인
#                     new_color = check_color(new_x)
#                     # 말 이동, 점수 추가
#                     if new_color > 0:  # 파란색일 경우 0번 인덱스
#                         location[i] = [0, new_color]
#                         new_grade += 10*new_color
#                     else:
#                         location[i] = [new_x, new_color]
#                         new_grade += 2*new_x

#             elif color == 1:
#                 new_x = x+dice[idx]
#                 # i번째 주사위를 던져 도착한 경우
#                 if new_x > 7:
#                     location[i][0] = -1
#                 else:
#                     # 가려고 하는 위치에 다른 말이 있는지 확인
#                     if not check_location(location, new_x, color, blue1[new_x]):
#                         continue
#                     # 말 이동, 점수 추가
#                     location[i] = [new_x, color]
#                     new_grade += blue1[new_x]

#             elif color == 2:
#                 new_x = x+dice[idx]
#                 # i번째 주사위를 던져 도착한 경우
#                 if new_x > 6:
#                     location[i][0] = -1
#                 else:
#                     # 가려고 하는 위치에 다른 말이 있는지 확인
#                     if not check_location(location, new_x, color, blue2[new_x]):
#                         continue
#                     # 말 이동, 점수 추가
#                     location[i] = [new_x, color]
#                     new_grade += blue2[new_x]

#             else:
#                 new_x = x+dice[idx]
#                 # i번째 주사위를 던져 도착한 경우
#                 if new_x > 7:
#                     location[i][0] = -1
#                 else:
#                     # 가려고 하는 위치에 다른 말이 있는지 확인
#                     if not check_location(location, new_x, color, blue3[new_x]):
#                         continue
#                     # 말 이동, 점수 추가
#                     location[i] = [new_x, color]
#                     new_grade += blue3[new_x]

#         solution(idx+1, location, new_grade)
#         location[i] = [x, color]


# if __name__ == '__main__':
#     dice = list(map(int, input().split()))
#     result = 0

#     blue1 = [10, 13, 16, 19, 25, 30, 35, 40]
#     blue2 = [20, 22, 24, 25, 30, 35, 40]
#     blue3 = [30, 28, 27, 26, 25, 30, 35, 40]

#     # parameter
#     # 1) 현재 주사위 순서
#     # 2) [i번째 말의 위치, i번째 말의 색]
#     # 3) 점수
#     solution(0, [[0,0], [0,0], [0,0], [0,0]], 0)
#     print(result)