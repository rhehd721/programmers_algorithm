# -*- coding: utf-8 -*- 
# K는 0 이상 1,000,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# Solutions
# 1. 가장작은 숫자와 두번째로 작은 숫자를 찾아야한다
# 2. 새로만든 맵기가 k를 넘는지 수시로 확인해야한다
# 3. 모든 결과가 만족하지 못할경우 -1을 반환한다

# scoville의 길이는 2 이상 1,000,000 이하입니다. scoville[0,1], scoville[0,1,.....1,000,000]
# K는 0 이상 1,000,000,000 이하입니다.  K = 0, ..... K = 1,000,000,000
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

def solution(scoville, K):
    answer = 0
    NewScoville = 0
    scoville.sort()

    for i in scoville:
        if(len(scoville) >= 2):
            NewScoville = scoville[0] + (scoville[1] * 2)
            del scoville[1]
            del scoville[0]
            scoville.append(NewScoville)
            answer += 1
            scoville.sort()
            if(scoville[0] > K):
                print("answer : ",answer)
                return answer
            else:
                continue
        else:
            if(scoville[0] > K):
                break
            else:
                print("answer : ", -1)
                return -1

    print("answer : ",answer)
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3, 9, 10, 12], 0))
print(solution([1, 2], 1000000000))
print(solution([0, 0], 1000000000))
print(solution([0, 1000000000], 1000000000))
print(solution([0, 0,0,0], 1000000000))
print(solution([100000000,100000000,100000000], 10000))
print(solution([8, 2, 3, 9, 10, 12], 7))