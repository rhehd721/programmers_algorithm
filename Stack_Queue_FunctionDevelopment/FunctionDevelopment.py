# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다
def solution(progresses, speeds):
    answer = []

    while True:
        # 일단 스피드와 개발정도를 더해준다
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        # 배포조건이 만족한다면 몇개가 배포가능한지 체크한다
        if (progresses[0] >= 100):
            check = 0
            for i in range(len(speeds)):
                if(progresses[i] >= 100):
                    check += 1
                else:
                    break
            answer.append(check)
            # 배포갯수를 확인하였으니 배포한건 리스트에서 지워준다
            for i in range(check):
                del progresses[0]
                del speeds[0]
            
        if (len(progresses) == 0):
            break

            
    
    return answer



progresses	= [93, 30, 55]

speeds = [1, 30, 5]	

solution(progresses, speeds)

# return = [2, 1]

progresses = [95, 90, 99, 99, 80, 99]

speeds = [1, 1, 1, 1, 1, 1]	

solution(progresses, speeds)

# return = [1, 3, 2]
