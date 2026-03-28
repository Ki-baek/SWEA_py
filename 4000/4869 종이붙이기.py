T = int(input())

paper = [0] * 31

paper[1]  =1

for i in range(2, 31):
  if i % 2 == 0:
    paper[i] = (paper[i - 1] * 2) + 1
  else:
    paper[i] = (paper[i - 1] * 2) - 1

for t in range(1, T + 1):
  N = int(input())
  
  N = N // 10
  print(f'#{t} {paper[N]}')