#day-4
#merge two arrays. [inplace]
def MergeArrays(array1,array2): 
    m=len(array1)-1
    for i in range(m,-1,-1):
        key=array1[-1]
        j=m-1
        while (j>=0 and array1[j]>array2[i]):
            array1[j+1]=array1[j]
            j=j-1
        if (key>array2[i]):
            array1[j+1]=array2[i]
            array2[i]=key

array1=[1, 3, 5]
array2=[2, 4, 6]
MergeArrays(array1,array2)
print("First List:",array1)
print("Second List:",array2)

        
