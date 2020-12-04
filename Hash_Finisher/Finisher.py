# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다. 즉, 무조건 한명만 완주못함
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

def solution(participant, completion):
    # 명단 정렬
    pa = sorted(participant)
    co = sorted(completion)
    a = 0
    answer = 0

    # 한명밖에 참가하지 않았다면 그사람이 미완주자
    if(len(pa) == 1):
        answer = pa[0]

    # 완주자 명단을 순회
    for i in range(len(co)):
        # 정렬한 두 리스트가 다른값이 나올때
        if (pa[i] != co[i]):
            a = 1
        if (a == 1 ):
            answer = pa[i]
            break
        # 정렬에 끝사람이 미완주자일때
        if (i == len(co)-1):
            if(a != 1):
                answer = pa[len(pa)-1]

    return answer


participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
solution(participant, completion)
# return =leo

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']
solution(participant, completion)
# return = vinko

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
solution(participant, completion)
# return = mislav

participant = ['mislav']
completion = []
solution(participant, completion)

