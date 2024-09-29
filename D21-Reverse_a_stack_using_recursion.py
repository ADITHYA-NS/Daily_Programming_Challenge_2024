# Day 21
# Reverse a stack using recursion
def reverse(stack):
    if len(stack)==0:
        return
    temp=stack.pop()
    reverse(stack)
    insertAtBottom(stack,temp)

def insertAtBottom(stack,temp):
    if len(stack)==0:
        stack.append(temp)
        return
    temp2=stack.pop()
    insertAtBottom(stack,temp)
    stack.append(temp2)

stack= [3, 2, 1]
reverse(stack)
print("reversed Stack:",stack)
