# Heap - Camouflage

## 최우수 풀이
```python
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
```

## 풀이 해석
- from collections import Counter
```python
cnt = Counter([kind for name, kind in clothes]) # 이부분을 통해 옷의 종류마다 갯수를 파악
```
- reduce(function, iterable, initializer)
    - iterable 의 요소들을 function 에 대입
    - initializer == 초기값
```python
reduce(lambda x, y: x*(y+1), cnt.values(), 1)
# cnt.values()의 값들을 x*(y+1)삭에 대입할것이며 초기값은 1이다.
```
