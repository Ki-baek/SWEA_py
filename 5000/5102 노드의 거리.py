from collections import deque

def bfs(start, end):
  if start == end:
    return 0
  
  queue = deque([start])
  cnt = 1
  lst = []
  judge = False
  while queue:
    
    k = queue.popleft()
    
    if end in node[k]:
      judge = True
      break
    
    elif visited[k] == 0:
      lst.extend(node[k])
      visited[k] += 1

    if not queue:
      queue.extend(lst)
      lst = []
      cnt += 1
      
  if judge:
    return cnt
  
  else:
    return 0

T = int(input())

for t in range(1, T + 1):
  v, e = map(int, input().split())
  
  node = [[] for _ in range(v + 1)]
  
  for i in range(e):
    a, b = map(int, input().split())
    
    node[a].append(b)
    node[b].append(a)
    
  s, g = map(int, input().split())
  
  visited = [0] * (v + 1)
  
  print(f'#{t} {bfs(s, g)}')