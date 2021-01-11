## 문제를 통해 알게된 개념

---

## Best 우수풀의
``` python
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
``` 
---
## 우수풀의 해석

// 나누기 연산 후 소숫점을 버리고 정수부분만 취함

** 거듭 제곱

---

## 다른 우수풀의
``` python
def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)
```

