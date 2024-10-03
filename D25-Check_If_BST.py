# Day 25
# Check if a Binary Tree is a Binary Search Tree (BST)
def isBST(arr):
    def inOrder(index):
        if index>=len(arr) or arr[index] is None:
            return []
        
        left=inOrder(2*index+1)
        current=[arr[index]]
        right=inOrder(2*index+2)
        return left+current+right
    inOrderList=inOrder(0)

    for i in range(1, len(inOrderList)):
        if inOrderList[i]<=inOrderList[i - 1]:
            return False     
    return True  
array = [10, 5, 15, None, None, 6, 20]
print(isBST(array))  
