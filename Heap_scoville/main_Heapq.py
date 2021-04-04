# -*- coding: utf-8 -*- 
# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while(1):
        if(scoville[0] >= K):
            print( 'answer : ' , answer)
            return answer
        else:
            if(len(scoville) >= 2):
                answer += 1
                new = heapq.heappop(scoville) + ( heapq.heappop(scoville) * 2 )
                heapq.heappush(scoville, new)
            else:
                print( 'answer : ' , -1)
                return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3, 9, 10, 12], 0))
print(solution([1, 2], 1000000000))
# print(solution([0, 0], 1000000000))
# print(solution([0, 1000000000], 1000000000))
# print(solution([0, 0,0,0], 1000000000))
# print(solution([100000000,100000000,100000000], 10000))
# print(solution([8, 2, 3, 9, 10, 12], 7))