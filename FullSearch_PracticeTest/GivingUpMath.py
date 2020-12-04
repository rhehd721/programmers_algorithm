# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    answer = []
    result = []

    # 학생들의 찍는 방식
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 학생들의 찍는 방식이 무한반복 될수있도록 체크하는 변수
    student1_Check = 0
    student2_Check = 0
    student3_Check = 0

    # 학생들의 최종점수
    student1_Score = 0
    student2_Score = 0
    student3_Score = 0


    for i in range(len(answers)):
        # 찍은것과 답이 같다면 점수를 더해준다
        if (answers[i] == student1[student1_Check]):
            student1_Score += 1
        
        if (answers[i] == student2[student2_Check]):
            student2_Score += 1

        if (answers[i] == student3[student3_Check]):
            student3_Score += 1

        # 학생들 점수 리스트가 변할 수 있게 변수에 1을 더해준다
        student1_Check += 1
        student2_Check += 1
        student3_Check += 1

        # 리스트가 반복될수 있도록 변수를 초기화해준다
        if(student1_Check == len(student1)):
            student1_Check = 0
        if(student2_Check == len(student2)):
            student2_Check = 0
        if(student3_Check == len(student3)):
            student3_Check = 0

    # 모든 점수들을 결과리스트에 넣어준다
    result.append(student1_Score)
    result.append(student2_Score)
    result.append(student3_Score)


    # 점수중 최대값을 학생들 점수와 비교해서 최고점을 획득한 학생을 추가해준다
    if (max(result) == student1_Score):
        answer.append(1)
    if (max(result) == student2_Score):
        answer.append(2)
    if (max(result) == student3_Score):
        answer.append(3)

    return answer

    # print(answer)


answers	 = [1,2,3,4,5]	

solution(answers)

# return = [1]


answers	 = [1,3,2,4,2]	

solution(answers)

# return = [1,2,3]

answers	 = [5]	

solution(answers)

answers	 = [1,3,2,4,2,1,3,2,4,2,3,2,4,2,1,3,2,4,2,3,2,4,2,1,3,2,4,2,3,2,4,2,1,3,2,4,2,3,2,4,2,1,3,2,4,2]	

solution(answers)