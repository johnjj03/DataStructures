def isValid(s) -> bool:
    check=[]
    # opening_brackets  = ['(','[','{']
    # closing_brackets = [')',']','}']
    brackets = {'(':')','{':'}','[':']'}
    for char in s:
        if(char in brackets):
            check.append(char)
        elif(char in brackets.values()):
            if(len(check) == 0 or check.pop() != brackets[char]):
                return False
        if(len(check) == 0):
            return True
    else:
        return False
            