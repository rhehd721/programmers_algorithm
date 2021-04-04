# Heap - Scoville

## 최우수 풀이
```python
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
```

## heapq
- 원소 추가
    - heapq.heappush(heap, 4)
- 원소 삭제
    - heapq.heappop(heap)
- 참조
    - heap[0]

리스트를 heap으로 변환
```python
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
```