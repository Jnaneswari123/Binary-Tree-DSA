class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preOrder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
preOrder(root)