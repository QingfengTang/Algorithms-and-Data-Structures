'''
操作给定的二叉树，将其变换为源二叉树的镜像 
'''
class TreeNode():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None
    
    def Mirror(self, root):
        '''
        每次迭代时交换左右子树.相当于将真个树的分解为 只关注 三个节点 temp, temp.left, temp.right的交换
        '''
        if not root:
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.Mirror(root.left)
        self.Mirror(root.right)

        return root
