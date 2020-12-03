# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []

    # prices 마지막-1 번까지 돌아라
    for i in range(0, len(prices)):
        # return에 넣어줄 값
        check = 0

        for j in range(i+1, len(prices)):
            # 값이 같거나 올랐으면
            if (prices[i] <= prices[j]):
                check += 1
            # 값이 떨어졌으면
            else:
                check += 1
                break
        

        answer.append(check)

    return answer


solution(prices)

prices = [1, 1]
solution(prices)

prices = [10000, 100]
solution(prices)

prices = [1, 10000, 1, 10000, 1]
solution(prices)




# return [4, 3, 1, 1, 0]

