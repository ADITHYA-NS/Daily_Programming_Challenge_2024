#day-3
#find duplicate number. we use same logic as finding a cycle in linked list
def Duplicate(array):
    slow=fast=0 
    slow=array[slow]
    fast=array[array[fast]]
    while(slow!=fast): #when both fast and slow points to same element, it means that there exists a duplicate number here
        slow=array[slow]
        fast=array[array[fast]]
    new_slow=0
    while(new_slow!=slow): #to find the duplicate element.
        new_slow=array[new_slow]
        slow=array[slow]
    return slow

array=  [3, 1, 3, 4, 2]
duplicate=Duplicate(array)
print("Duplicate:",duplicate)
