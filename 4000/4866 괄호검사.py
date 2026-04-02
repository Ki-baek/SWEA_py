from collections import deque

T = int(input())

pair = {')': '(', '}': '{'}

for t in range(1, T + 1):
  string = deque(input().strip())
  stack = []
  judge = True
  
  while string:
    a = string.popleft()
    
    # if a =="\'" or a == "\"":
    #   pass 
    if a in pair.values():
      stack.append(a)
    elif a in pair.keys():
      if stack and stack[-1] == pair[a]:
        stack.pop()
      else: judge = False

    
  if judge and not stack:
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')