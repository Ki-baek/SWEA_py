def dfs(stx, sty):
  global ans
  
  
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  
  

  for i in range(4):

    nowX = stx + dx[i]
    nowY = sty + dy[i]
    
    if 0 <= nowX < n and 0 <= nowY < n:
      if maze[nowY][nowX] == 0 and visited[nowY][nowX] == 0 :
        visited[nowY][nowX] += 1
        dfs(nowX, nowY)
      elif maze[nowY][nowX] == 3:
        ans = 1
        return

  
    


T = int(input())

for t in range(1, T + 1):
  n = int(input())
  ans = 0
  maze = [list(map(int, input().rstrip())) for _ in range(n)]
  
  for y in range(n):
    for x in range(n):
      if maze[y][x] == 2:
        startX, startY = x, y
        
  
  visited = [[0 for i in range(n)] for _ in range(n)]
  
  dfs(startX, startY)
  
  print(f'#{t} {ans}')