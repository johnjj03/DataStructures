def isValid(s) -> bool:
    check=[]
    for i in s:
        if(i in ['(','[','{']):
            check.append(i)
        elif(i in [')',']','}'] and len(check) == 0):
            return False
        if(i == ')'  and check.pop() != '('):
            return False
        elif(i == ']' and check.pop() != '['):
            return False
        elif(i == '}' and check.pop() != '{'):
            return False
        if(len(check) == 0):
            return True
    else:
        return False
            