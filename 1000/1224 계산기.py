for t in range(1, 11):
  n = int(input())
  
  lst = list((input()))
  
  stack = []
  
  postfix = []
  
  for i in range(n):
    if lst[i] == '(':
      stack.append('(')
      
    elif lst[i] == '*':
      if stack[-1] == '*':
        postfix.append('*')
      else:
        stack.append('*')
      
    elif lst[i] == '+':
      if stack[-1] != '(':
        postfix.append(stack.pop())
        stack.append('+')
      else:
        stack.append('+')
        
    elif lst[i] == ')':
      pop = stack.pop()
      
      while pop != '(':
        postfix.append(pop)
        pop = stack.pop()
        
    else:
      postfix.append(lst[i])
  
  
  output_stack = []
  
  for i in (postfix):
    if i == '*':
      a = output_stack.pop()
      b = output_stack.pop()
      
      output_stack.append(a * b)
    elif i == '+':
      a = output_stack.pop()
      b = output_stack.pop()
      
      output_stack.append(a + b)
    else:
      output_stack.append(int(i))
  
  print(f'#{t} {output_stack.pop()}')