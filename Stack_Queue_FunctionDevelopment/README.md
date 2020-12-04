## Best 우수풀의
``` python
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
``` 
---
## 우수풀의 해석

### zip()

zip() : zip()은 내장함수로 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환을 해주는 역할을 한다.

### Operator

![screensh](./Operator.png)

---


