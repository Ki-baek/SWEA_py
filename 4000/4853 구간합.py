t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  lst = list(map(int, input().split()))
  preSum = []
  
  for j in range(n - m + 1):
    preSum.append(sum(lst[j : j + m]))
    
  print(f'#{i + 1} {max(preSum)-min(preSum)}')
  

'''0번 1번 2번
1번 2번 3번
0 + i 라고 하면 i 가 0부터 n - m + 1 인 list 까지 
연산 및 max값 구하기
시간 초과? 최대 연산 횟수가 case당 98회 +
case 최대 50가지 = 초과 안될거 같음
min 값은 어떻게 비교할 것인가? 처음 한값을 min judge로 만들어두고 시작을 하자.
그러면 i = 1부터 하고 i = 0일때의 값을 min/max_judge로 쓰면 for 문 하나에 정리되겠다
________________________아니 그냥 presum을 해두고 거기서 min/max()를 이용해서 하는게 낫겠다_________________________
j = 0 일때 0 + 0 삼중for ? 는 진짜 큰일남 전체 문자열 길이가 10이면 01234 12345 --- 56789 슬라이싱


'''