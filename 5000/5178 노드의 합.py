T = int(input())


for t in range(1, T + 1):
  n, m, l = map(int, input().split())

  tree = [0] * (n + 1)

  for i in range(m):
    a, b = map(int, input().split())
    
    tree[a] = b
    
  for i in range(n, 1, -1):
    tree[i // 2] += tree[i]
  
  print(f'#{t} {tree[l]}')