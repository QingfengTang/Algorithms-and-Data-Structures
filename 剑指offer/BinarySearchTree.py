'''
二叉搜索树(BST)
'''
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST():
    def PreOrder(self, root):
        '''
        前序遍历
        '''
        if root:
            print(root.val, end=' ')
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def RecursionFind(self, root, x):
        '''
        在BST中查找x
        递归实现
        '''
        if not root:
            return False
        
        if root.val > x:
            return self.RecursionFind(root.left, x)
        elif root.val < x:
            return self.RecursionFind(root.right, x)
        else:
            return True
    
    def NonRecursionFind(self, root, x):
        '''
        非递归实现查找
        '''
        if not root:
            return False
        while root:
            if root.val > x:
                root = root.left
            elif root.val < x:
                root = root.right
            else:
                return True
        return False
    
    def NoneRecursionFindMin(self, root):
        '''
        非递归实现找最小值
        最左面的结点为最小值
        '''
        if not root:
            return None
        while root:
            node = root
            root = root.left
        return node
    
    def RecursionFindMin(self, root):
        '''
        递归实现找最小值
        '''
        if not root:
            return None
        # 如果左结点为空则此时的根为最小
        if not root.left:
            return root
        else:
            return self.RecursionFindMin(root.left)
    
    def RecursionFindMax(self, root):
        '''
        找最大值
        最右面的结点为最大值
        '''
        if not root:
            return None
        if root.right:
            return self.RecursionFindMax(root.right)
        else:
            return root
    
    def InsertNode(self, root, x):
        '''
        插入结点时要保证插入后依然为搜索树
        '''
        if not root:
            root = TreeNode(x)
        else:
            if root.val > x:
                root.left = self.InsertNode(root.left, x)
            if root.val < x:
                root.right = self.InsertNode(root.right, x)
        # 如果x已经存在啥都不做
        return root
    
    def DeleteNode(self, root, x):
        '''
        删除搜索树中的节点 先查再删
        删的时候考虑三种情况 1.删除节点为叶子节点 2.删除节点有一个子节点 3.删除节点有两个子结点
        '''
        if not root:
            return None
        
        else:
            if root.val < x:
                root.right = self.DeleteNode(root.right, x)
            elif root.val > x:
                root.left = self.DeleteNode(root.left, x)
            else:
                # 有两个结点，找左树的最大值或者右树的最小值
                if root.left and root.right:
                    temp = self.RecursionFindMin(root.right)
                    root.val = temp.val
                    root.right = self.DeleteNode(temp, temp.val)
                else:
                    # 有一个节点或者一个节点都没
                    if not root.right:
                        root = root.right
                    else:
                        root = root.left

        return root
                    
        
        


    




if __name__ == '__main__':
    vals = [18, 10, 20, 7, 15, 22, 9]
    A, B, C, D, E, F, G = [TreeNode(i) for i in vals]
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F
    D.right = G
    BStree = BST()
    print('前序遍历')
    BStree.PreOrder(A)
    print('\n递归实现查找')
    print(BStree.RecursionFind(A, 7))
    print('非递归实现查找')
    print(BStree.NonRecursionFind(A, 7))
    print('递归找最小值')
    print(BStree.RecursionFindMin(A).val)
    print('非递归找最小值')
    print(BStree.NoneRecursionFindMin(A).val)
    print('找最大值')
    print(BStree.RecursionFindMax(A).val)
    print('插入结点')
    BStree.InsertNode(A, 6)
    BStree.PreOrder(A)
    print('删除节点')
    BStree.DeleteNode(A,6)
    BStree.PreOrder(A)

