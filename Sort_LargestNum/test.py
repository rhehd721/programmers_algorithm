def solution(people, limit):
    answer = 0

    people.sort(reverse=1)

    while(1):
        for i in (0, len(people) -1):
            check = 0
            tttt = 0
            if(people[i] != -1):
                tttt = 0
                weight = people[i]
                num = i
                for j in (i, len(people) -1):
                    if (people[j] == -1):
                        continue
                    else:
                        if (weight + people[j] > limit):
                            continue
                        else:
                            people[i] = -1
                            people[j] = -1
                            check = 1
                            break
            else:
                tttt = 1
        if(check):
            print("two exit")
        else:
            people[num] = -1
            print("one exit")
        if(tttt):
            print("answer : ", answer)
            return answer
        answer += 1
            

    print("answer : ", answer)
    return answer

people = [70, 50, 80, 50]
limit = 100
solution(people, limit) # 3

people = [70, 80, 50]
limit = 100
solution(people, limit) # 3

