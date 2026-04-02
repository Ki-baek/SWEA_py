def dfs(stx, sty):
  
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  
    


T = int(input())

for t in range(T):
  n = int(input())
  
  maze = [list(map(int, input().split())) for _ in range(n)]
  
  for y in range(n):
    for x in range(n):
      if maze[y][x] == 2:
        startX, startY = x, y
        
  
  visited = [[0 for i in range(n)]for _ in range(n)]
  
  dfs(startX, startY)