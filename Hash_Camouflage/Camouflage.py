# -*- coding: utf-8 -*- 
# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.

def solution(clothes):
    answer = 0
    dic = {}
    for i in clothes:
        if(None == dic.get(i[1])):
            dic.update({i[1] : 1})
        else:
            dic.update({i[1] : dic[i[1]] + 1})
    
    
    if(len(dic) == 1):  # 한종류라면
        for i in dic:
            answer += dic.get(i)
        print(answer)
        return answer
    else:   # 옷이 여러 종류라면
        answer = 1
        for i in dic:
            answer *= (dic.get(i) + 1)  # 갯수 + 안입는 경우
        print(answer - 1)   # -1 의 이유는 적어도 1개의 옷은 선택해야 하기 때문
        return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes) #	5
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
solution(clothes) #	3