def evalRPN(tokens) -> int:
      stack = []
      ops = {'+','-','*','/'}
      for i in tokens:
          if i not in ops:
            stack.append(int(i))
          elif len(stack) > 1:
            if i == "+":
              stack.append(stack.pop()+stack.pop())
            elif i == "-":
              stack.append(-(stack.pop()-stack.pop()))
            elif i == "*":
              stack.append(stack.pop()*stack.pop())
            else:
              a = stack.pop()
              b = stack.pop()
              stack.append(int(b/a))
      return stack[0]

print(evalRPN(["2", "1", "+", "3", "*"])) # 9