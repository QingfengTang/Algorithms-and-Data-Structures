'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None
    

class solution():
    '''
    要判断B是不是A的子树，首先肯定要遍历A树，判断A的某个节点是不是和B的节点相同，如果相同，再判断以B为根节点的左右子树是否和A的相同
    '''
    def CalhasSubtree(self, pRootA, pRootB):
        result = False
        if pRootA and pRootA:
            if pRootA.val == pRootB.val:
                result = self.doTree1HaveTree2(pRootA, pRootB)
            if not result:
                result = self.doTree1HaveTree2(pRootA.left, pRootB)
            if not result:
                result = self.doTree1HaveTree2(pRootA.right, pRootB)
        
        return result

    def doTree1HaveTree2(self, pRootA, pRootB):
        # note:这里的两个if不能调换顺序，考虑当前A和B都是叶子节点的情况，如果先判断A会返回False,但此时A和B是相等的
        if not pRootB:
            return True
        if not pRootA:
            return False
        if pRootA.val != pRootB.val:
            return False
        
        return self.doTree1HaveTree2(pRootA.left, pRootB.left) and self.doTree1HaveTree2(pRootA.right, pRootB.right)
