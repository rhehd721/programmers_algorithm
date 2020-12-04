# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.

# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.

def solution(array, commands):
    answer = []

    for i in range(0, len(commands)):
        array2 = list(array)


        # 뒷쪽 지우기
        for k in range(commands[i][1], len(array)):
            del array2[commands[i][1]]

        # 앞쪽 지우기
        for j in range(0, commands[i][0]-1):
            del array2[0]

        # 앞뒤를 지운 리스트 정렬하기
        array2.sort()

        
        # 정렬한 리스트에서 n번째 숫자를  찾아 answer에 추가
        answer.append(array2[commands[i][2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# [5, 6, 3]

solution(array, commands)
