import heapq
from collections import deque


T = int(input())

for t in range(1, T + 1):
  n = int(input())
  result = 0
  heap = []
  lst = deque(map(int, input().split()))
  
  while lst:
    k = lst.popleft()
    heapq.heappush(heap, k)
  
  while n > 1:
    n //= 2
    result += heap[n - 1]
  
  print(f'#{t} {result}')