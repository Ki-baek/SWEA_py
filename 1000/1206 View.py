for j in range(10):
  result = 0
  n = int(input().strip())

  apt = list(map(int, input().rstrip().split()))
  
  for i in range(2, n - 2):
    
    if apt[i - 2] < apt[i] and apt[i - 1] < apt[i] and apt[i + 1] < apt[i] and apt[i + 2] < apt[i]:
      view = apt[i] - max(apt[i - 2], apt[i - 1], apt[i + 1], apt[i + 2])
      result += view
    else:
      continue
  
  print(f'#{j + 1} {result}')








'''
층수 255 최대 이고
건물수 최대 1000 물론 -4이지만
케이스 10개라고 확정
그럼 lst[i-2] i-1 i i+1 i+2 라하면 996 * 255 * 10 = 300만 정도 나옴
이정도면 그냥 이차원 배열 박아도 될거 같은데..
'''