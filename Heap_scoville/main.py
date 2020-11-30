# K는 0 이상 1,000,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# Solutions
# 1. 가장작은 숫자와 두번째로 작은 숫자를 찾아야한다
# 2. 새로만든 맵기가 k를 넘는지 수시로 확인해야한다
# 3. 모든 결과가 만족하지 못할경우 -1을 반환한다

# 제일중요한 과정! (새로만든 음식을 리스트 중간에 넣어주어야한다!)

# scoville의 길이는 2 이상 1,000,000 이하입니다. scoville[0,1], scoville[0,1,.....1,000,000]
# K는 0 이상 1,000,000,000 이하입니다.  K = 0, ..... K = 1,000,000,000
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

def solution(scoville, K):
    Check = 0
    scoville.sort()

    if (scoville[0] == 0):
        scoville.remove(0)
        if (scoville[0] >= K):
            return 1
    elif (scoville[0] >= K):
        return 0

    while (len(scoville) >= 2):
        # 제일작은 두개로 작업해라
        scoville[1] = scoville[0] + (scoville[1] * 2)
        del scoville[0]
        # 섞은회수 증가!
        Check += 1

        # 정렬해라
        scoville.sort()

        # 섞은다음부터 커지게되면 종료해라
        if (scoville[0] >= K):
            break
        # 더이상 더할 두개가 없어졌다면
        elif (len(scoville) == 1):
            Check = 0
            break

    if(Check == 0):
        answer = -1
    else:
        answer = Check
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3, 9, 10, 12], 0))
print(solution([1, 2], 1000000000))
print(solution([0, 0], 1000000000))
print(solution([0, 1000000000], 1000000000))
print(solution([0, 0,0,0], 1000000000))
print(solution([100000000,100000000,100000000], 10000))
print(solution([8, 2, 3, 9, 10, 12], 7))