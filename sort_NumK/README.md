# 문제를 통해 알게된 개념
python에 깊은복사와 얕은 복사가 존재한다.

---

## Best 우수풀의
``` python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

---
## 우수풀의 해석

### lambda
(lambda x,y: x + y)(10, 20) 
result = 30

### map
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
a
result = [1, 2, 3, 4]

---
## 다른 풀의법
``` python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
``` 