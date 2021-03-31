def solution(people, limit):
    answer = 0

    people.sort(reverse=1)

    while(1):
        if(len(people) >= 2):
            for i in (1, len(people) -1):
                check = 0
                weight = people[0] + people[i]
                if(weight > limit):
                    continue
                else:
                    del people[i]
                    del people[0]
                    check = 1
                    break
            if(check):
                print("two exit")
                print(len(people))
            else:
                del people[0]
                print("one exit")
                print(len(people))
            answer += 1
            if(len(people) == 0):
                print("answer : ", answer)
                return answer
        else:
            answer += 1
            break

    print("answer : ", answer)
    return answer

people = [70, 50, 80, 50]
limit = 100
solution(people, limit) # 3

people = [70, 80, 50]
limit = 100
solution(people, limit) # 3

