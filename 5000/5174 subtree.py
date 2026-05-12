from collections import deque

T = int(input())

for t in range(1, T + 1):
  E, N = map(int, input().split())
  result = 1
  
  tree = [[0] * 3 for _ in range(E + 2)]
  node = list(map(int, input().split()))
  
  for i in range(E):
    if tree[node[i * 2]][1] == 0:
      tree[node[i * 2]] [1]= node[i * 2 + 1]
    else:
      tree[node[i * 2]][2] = node[i * 2 + 1]
    
  queue = deque([N])
  
  while queue:  
      k = queue.popleft()
      if tree[k][1] != 0:
        queue.append(tree[k][1])
        result += 1
      if tree[k][2] != 0:
        queue.append(tree[k][2])
        result += 1
        
  print(f'#{t} {result}')