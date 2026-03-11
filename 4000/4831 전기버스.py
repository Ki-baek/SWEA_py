t = int(input())

for i in range(t):
  k, n, m = map(int,input().split())
  
  bus_stop = [0] * (n + 1)
  lst = list(map(int, input().split()))
  
  for j in lst:
    bus_stop[j] = 1
  
  locate = 0
  cnt = 0
  
  while locate + k < n:
    judge = False
    
    for l in range(k, 0, -1):
      if bus_stop[locate + l] == 1:
        cnt += 1
        locate += l
        judge = True
        break
    if not judge:
      cnt = 0
      break

  print (f'#{i + 1} {cnt}')
    
  


'''
정류장 받으면
bus_stop = [0] * 정류장수 미리 정의
받은 값의 bus stop[i] = 1로 변환
한번에 갈수 있는 거리가 k로 정해져 있으니
if bus_stop[k] = 1
->멈추고 충전,위치 기록해주고 (locate 변수 추가 이용) cnt + =1 // locate = 0시작 n -1번 정류장까지
for 돌려서 -1 해가며 k범위 내에 충전기가 있는지 파악 해주고
없으면 0 출력하고 break
locate + k 가 >= 정류장 수 이면 종료? 반복문 돌리기 전에 종료
테스트 케이스 및 연산이 간단해서 시간 초과 안날듯
___________________________________________________________
짜다보니 삼중반복문......근데 케이스가 최대 50000개
절대 안됨

*** 그러면 m개의 정류장에서 현재 bus_stop[i] - locate 를 구해 그게 k보다 크면
    당연히 다음 저거 뭐냐 충전소까지 도착을 못하겠지 그럼 0
    근데 k보다 작으면 lst[i + 1] - locate 이 k 보다 작은지 확인 


'''