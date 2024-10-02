#Day 24
#Lowest Common Ancestor
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def lowestCommonAncestor(root,p,q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    
    return left if left else right
def buildTree(values):
    if not values:
        return None
    
    def inner(index):
        if index >= len(values) or values[index] is None:
            return None
        node = TreeNode(values[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner(0)
def findNode(root,value) :
    if not root:
        return None
    if root.val == value:
        return root
    left = findNode(root.left, value)
    if left:
        return left
    return findNode(root.right, value)
values=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root=buildTree(values)
p_val=5
q_val=4
p=findNode(root,p_val)
q=findNode(root,q_val)
output= lowestCommonAncestor(root,p,q)
print("Output:",output.val)  

    
