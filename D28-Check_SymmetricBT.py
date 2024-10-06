# Day 28
# Check if a binary tree is symmetric or not
def is_symmetric_array(arr):
    def is_mirror(lf, ri):
        if lf>=len(arr) and ri>=len(arr):
            return True
        if lf>=len(arr) or ri>=len(arr) or arr[lf]!=arr[ri] or arr[lf]==None or arr[ri]==None :
            return False
        return is_mirror(2*lf+1, 2*ri+2) and is_mirror(2*lf+2,2*ri+1)
    if not arr:
        return True
    return is_mirror(1, 2)

array= [1, 2, 2, 3, None, None, 3]
res=is_symmetric_array(array)
if res==True:
    print("Binary Tree is Symmetric")
else:
    print("Binary Tree is not symmetric")
