#Day 19
#Evaluate a Postfix Expression
def EvalPostfix(s):
    s=s.split()
    stack=[]
    operators="+-*/^"
    for i in s:
        print(stack)
        if i.lstrip('-').isdigit():  
            stack.append(int(i)) 
        elif i in operators:
            val1=stack.pop()
            val2=stack.pop()
            if i=='+':
                stack.append(val2+val1)
            elif i=='-':
                stack.append(val2-val1)
            elif i=='*':
                stack.append(val2*val1)
            elif i=='/':
                stack.append(int(val2/val1))
            elif i=='^': #what ^ does us not specified in question. So to get the mentioned outout, I assumed it to be power.
                  stack.append(val2**val1)

    return stack[0] if stack else None
s="3 4 2 * 1 5 - 2 3 ^ ^ / +"
print("Output:",EvalPostfix(s))
