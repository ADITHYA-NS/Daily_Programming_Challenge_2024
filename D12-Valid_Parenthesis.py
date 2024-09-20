# Day-12
# Valid parenthesis with multiple types
def ValidParenthesis(s):
    temp_stack=[]
    for i in s:
        if i=='[':
            temp_stack.append(']')
        elif i=='{':
            temp_stack.append('}')
        elif i=='(':
            temp_stack.append(')')
        else:
            if len(temp_stack)!=0 and i==temp_stack[-1]:
                temp_stack.pop(-1)
            else:
                return False
    if len(temp_stack)==0:
        return True
    else:
        return False
        
    
    
s = "[{()}]"
op=ValidParenthesis(s)
print(op)
