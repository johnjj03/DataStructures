def evalRPN(tokens) -> int:
      stack = []
      ops = {'+','-','*','/'}
      for i in tokens:
          if i not in ops:
            stack.append(int(i))
          elif len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if i == "+":
              stack.append(a+b)
            elif i == "-":
              stack.append(b-a)
            elif i == "*":
              stack.append(a*b)
            else:
              stack.append(int(b/a))
      return stack[0]

print(evalRPN(["2", "1", "+", "3", "*"])) # 9