#Day 20
#Sort Stack using recursion
def sortStack(stack):
    if len(stack)==0:
        return
    temp=stack.pop()
    sortStack(stack)
    insertAtpos(temp,stack)

def insertAtpos(temp,stack):
    if len(stack)==0 or temp>stack[-1]:
        stack.append(temp)
        return
    elem=stack.pop()
    insertAtpos(temp,stack)
    stack.append(elem)
stack=[3, 1, 4, 2]
sortStack(stack)
print("Sorted Stack:",stack)
