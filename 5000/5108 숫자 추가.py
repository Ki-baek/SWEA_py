T = int(input())

for t in range(1, T + 1):
  n, m, l = map(int, input().split())
  
  
  lst = list(map(int, input().split()))
  
  for i in range(m):
    a, b = map(int, input().split())
    lst.insert(a, b)
  
  print(f"#{t} {lst[l]}")