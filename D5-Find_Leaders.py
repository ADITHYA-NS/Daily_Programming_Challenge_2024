#Day 5
#find leader 
def FindLeader(array):
    leaders=[]
    greatest=-1
    for i in range(len(array)-1,-1,-1):
        if array[i]>greatest:
            greatest=array[i]
            leaders.append(greatest)
    leaders=leaders[::-1]
    return leaders

array=[7, 10, 4, 10, 6, 5, 2]
leaders=FindLeader(array)
print("Leaders:",leaders)  
    
