def solution(scoville, K):
    Check = 0
    # 처음에 정렬되어있지 않을 수 있다
    scoville.sort()
    
    # 효율을 위해 0값들을 지워주자
    if (scoville[0] == 0):
        scoville.remove(0)
        # 제일 작은수가 이미 K를 넘긴경우 종료하여주자(0이 존재했었으니 적어도 1 이상이다) ################ 망함(같은숫자들은 하나만 남기고 지워야한다)
        if (scoville[0] >= K):
            return 1
    # 제일 작은수가 이미 K를 넘긴경우 종료하여주자
    elif (scoville[0] >= K):
        return 0

    # list가 2개 이상이면 반복문을 실행해라
    while (len(scoville) >= 2):
        
        # 제일작은 두개로 작업해라
        scoville[1] = scoville[0] + (scoville[1] * 2)
        # 더해준 숫자는 없애준다
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

    # K를 초과하지 못할경우 -1
    if(Check == 0):
        answer = -1
    # K를 초과할경우 섞은 횟수
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
print(solution([0, 0,0,0, 1000], 100))

