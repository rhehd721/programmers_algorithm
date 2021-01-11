# -*- coding: utf-8 -*-
# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

# 완전탐색
# 한줄일때 두줄일때 세줄일때....
def solution(brown, yellow):
    width = 0
    height = 0

    # 꼭지점 4개를 제와
    count = (brown - 4)  / 2
    i = 1

    # 노란부분의 두께를 알아내는 과정
    while True:
        if (count - i) * i == yellow:
            width = (count - i) + 2
            height = i + 2
            break
        i = i+1


    answer = []
    answer.append(width)
    answer.append(height)
    return answer



print("첫번째 test")
brown = 10
yellow = 2
solution(brown, yellow)
# return = [4, 3]

print("두번째 test")
brown = 8
yellow = 1
solution(brown, yellow)
# return = [3, 3]

print("세번째 test")
brown = 24
yellow = 24
solution(brown, yellow)
# return = [8, 6]


