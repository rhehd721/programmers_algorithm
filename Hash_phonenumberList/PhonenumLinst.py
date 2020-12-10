# -*- coding: utf-8 -*- 


# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.

def solution(phone_book):
    answer = 0

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if(j == i ):
                pass
            else:
                answer = str(phone_book[j]).startswith(str(phone_book[i]))
                # print(answer)
                if(answer == True):
                    break
        if(answer != 0):
            break

    if (answer == True):
        answer = False
    elif (answer == False):
        answer = True
    elif (answer == 0):
        answer = True

    print(answer)


    return answer



phone_book = [119, 97674223, 1195524421]
solution(phone_book)
# false

phone_book = [123,456,789]
solution(phone_book)
# true

phone_book = [12,123,1235,567,88]
solution(phone_book)
# false

phone_book = [1]
solution(phone_book)
# true
