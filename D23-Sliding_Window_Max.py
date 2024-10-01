# Day 23
# Sliding Window Maximum
from collections import deque
def WindowMaxVal(array,k):
    max_val=[]
    Q=deque()
    for i in range(k):
        while Q and array[i]>=array[Q[-1]]:
            Q.pop()
        Q.append(i)
    for i in range(k,len(array)):
        max_val.append(array[Q[0]])
        while Q and Q[0] <= i-k:
            Q.popleft()
        while Q and array[i] >= array[Q[-1]]:
            Q.pop()
        Q.append(i)
    max_val.append(array[Q[0]])
    return max_val

array=[1, 3, -1, -3, 5, 3, 6, 7]
k=3
output=WindowMaxVal(array,k)
print("Max values:",output)

