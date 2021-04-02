# 아니 이것도 효율성이 아나오는건 너무한거 아니야고....


def solution(people, limit):
    answer = 0
    PointStrat = 0
    PointEnd = len(people)

    ExitNum = 0

    people.sort(reverse=1)  

    while(PointStrat <= PointEnd):
        answer += 1
        weight = people[PointStrat]
        # if(weight == 0):
        #     print("answer : ", answer -1 )
        #     return answer
        ExitNum = 1
        for i in range(PointStrat + 1, PointEnd):
            # print(i)
            # print(weight)
            weight2 = weight + people[i]
            if (weight2 > limit ):
                continue
            else:
                if(people[i] == 0):
                    continue
                else:
                    people[i] = 0
                    people[PointStrat] = 0
                    ExitNum = 2
                    break
        if(ExitNum == 2):
            ExitNum = 0
        else:
            people[PointStrat] = 0
        # for i in people:
        #     print(i)
        while(1):
            if(people[PointStrat] == 0):
                PointStrat += 1
                if(PointEnd -1 == PointStrat):
                    if(people[PointStrat] == 0):
                        print("answer : ", answer)
                        return answer
                    else:
                        print("answer : ", answer + 1)
                        return answer + 1
            else:
                break
    
    print("answer : ", answer)
    return answer

# main
people = [70, 50, 80, 50]
limit = 100
solution(people, limit) # 3

people = [70, 80, 50]
limit = 100
solution(people, limit) # 3

