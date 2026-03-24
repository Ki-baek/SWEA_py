t = int(input())

for tc in range(t):
  n, m = map(int, input().split())

  max_fly = -1
  
  area = [list(map(int, input().split())) for _ in range(n)]

  
  for y in range(n - m + 1):
    for x in range(n - m + 1):
      k = 0
      
      for i in range(m):
        
        k += sum(area[y + i][x : x + m])
      
      max_fly = max(max_fly, k)
  
  print(f'#{tc + 1} {max_fly}')