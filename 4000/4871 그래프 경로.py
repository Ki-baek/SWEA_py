def dfs(start, end):
  
  queue = [start]
  
  while queue:
    
    k = queue.pop()
    visited[k] = 1
    queue.extend(node[k])
    
  if visited[end] == 1:
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')


T = int(input())

for t in range(1, T + 1):
  V, E = map(int, input().split())
  visited = [0] * (V + 1)
  node = [[] for _ in range(V + 1)]
  for _ in range(E):
    a, b = map(int, input().split())
    
    node[a].append(b)
    
  S, G = map(int, input().split())
  
  dfs(S, G)