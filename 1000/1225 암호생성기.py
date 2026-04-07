from collections import deque

for _ in range(10):
  
  t = int(input())
  passwd = deque(map(int, input().split()))
  
  while True:
    
    for i in range(1, 6):
      if passwd[0] <= i:
        passwd[0] = 0
        passwd.rotate(-1)
        break
      
      else:
        passwd[0] -= i
        passwd.rotate(-1)
      
    if passwd[-1] == 0:
        break
      
      
  
  print(f'#{t}', *passwd)