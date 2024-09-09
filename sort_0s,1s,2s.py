def DNF(array): 
    if len(array)==0:
        return array
    start=mid=0
    end=len(array)-1
    while(mid<=end):
        if array[mid]==0:
            array[mid],array[start]=array[start],array[mid]
            start=start+1
            mid=mid+1
        elif array[mid]==1:
            mid=mid+1
        else:
            array[mid],array[end]=array[end],array[mid]
            end=end-1
array = [0, 1, 2, 1, 0, 2, 1, 0]
DNF(array)
print(array)