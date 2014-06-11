#! /usr/bin/python

def parse_to_infix(exp):
  ret = []
  start = 0
  just_right = False
  for i in range(0, len(exp)):
    char = exp[i]
    if char in ('('):
      ret.append(char)
      start = i+1
      just_right = False
    elif char in (')'):
      end = i
      if start<=end:
        number = exp[start:end]
        ret.append(int(number))
        ret.append(char)
      just_right = True
    elif char in ('+','-','*','/'):
      end = i
      if not just_right:
        if start<=end:
          number = exp[start:end]
          ret.append(int(number))
          ret.append(char)
          start = i+1
      else:
        ret.append(char)
        start = i+1
      just_right = False
    else:
      just_right = False
  if just_right:
    pass
  else:
    end = len(exp)
    if start<=end:
      number = exp[start:end]
      ret.append(int(number))
  if ret[len(ret)-1] in ('+','-','*','/'):
    raise Exception("not valid expresstion")
  return ret

def infix_to_postfix(arr):
  stack = []
  ret = []
  for ele in arr:
    if ele not in ('+','-','*','/','(',')'):
      ret.append(ele)
    else:
      if ele in ('+','-'):
        while len(stack)>0 and stack[len(stack)-1] != '(':
          ret.append(stack.pop())
        stack.append(ele)
      elif ele in ('*','/'):
        while len(stack)>0 and stack[len(stack)-1] in ('*', '/'):
          ret.append(stack.pop())
        stack.append(ele)
      elif ele == ')':
        while len(stack)>0 and stack[len(stack)-1] != '(':
          ret.append(stack.pop())
        if stack[len(stack)-1] == '(':
          stack.pop()
        else:
          raise Exception("')' not match '('")
      else:
        stack.append(ele)
  while len(stack)>0:
    ret.append(stack.pop())
  return ret  

def calculate(postfix):
  stack = []
  for item in postfix:
    if item in ('+','-','*','/'):
      right = stack.pop()
      left = stack.pop()
      if item == '+':
        stack.append(left+right)
      elif item == '-':
        stack.append(left-right)
      elif item == '*':
        stack.append(left*right)
      elif item == '/':
        stack.append(left/right)
    else:
      stack.append(item)
  return stack[0]

def main():
  exp = raw_input("exp:>")
  infix = parse_to_infix(exp)
  print infix
  #postfix = infix_to_postfix(['3','*','(','1','+','2',')'])
  postfix = infix_to_postfix(infix)
  print postfix
  ret = calculate(postfix)
  print ret

if __name__=='__main__':
  main()
