class TreeNode():
    '''
    二叉树节点
    '''
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def preOrder(root, prelist=[]):
    '''
    二叉树的前序遍历
    '''
    if root.data != None:
        prelist.append(root.data)
    if root.left != None:
        preOrder(root.left, prelist)
    if root.right != None:
        preOrder(root.right, prelist)
    
    return prelist

    

class BTree():
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
    
    def preOrder(self, prelist=[]):
        '''
        前序遍历 根->左->右
        '''
        
        if self.data != None:
            prelist.append(self.data)
            print(self.data, end=' ')
        if self.left != None:
            self.left.preOrder(prelist)
        
        if self.right != None:
            self.right.preOrder(prelist)
        
        return prelist
    
    def midOrder(self, midlist=[]):
        '''
        中序遍历 左->根->右
        '''
        if self.left != None:
            self.left.midOrder(midlist)
        if self.data != None:
            midlist.append(self.data)
            print(self.data, end=' ')
        if self.right != None:
            self.right.midOrder(midlist)
        
        return midlist
    
    def bacOrder(self, baclist=[]):
        '''
        后序遍历 左->右->根
        '''
        if self.left != None:
            self.left.bacOrder()
        if self.right != None:
            self.right.bacOrder()
        if self.data != None:
            baclist.append(self.data)
            print(self.data, end=' ')
        return baclist
    
    def reConstructBinaryTree(self, pre, mid):
        '''
        根据前序遍历和中序遍历重建二叉树
        '''
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            node = TreeNode(pre[0])
            node.left = self.reConstructBinaryTree(pre[1: mid.index(pre[0])+1], mid[: mid.index(pre[0])])
            node.right = self.reConstructBinaryTree(pre[mid.index(pre[0])+1 :], mid[mid.index(pre[0])+1 :])

        return node
        


if __name__ == '__main__':
    # 创建二叉树 A为根节点
    A, B, C, D, E, F, G = [BTree(i) for i in 'abcdefg']
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    print('前序遍历')
    prelist = A.preOrder()
    print('\n中序遍历')
    midlist = A.midOrder()
    print('\n后序遍历')
    baclist = A.bacOrder()
    print('\n根据前和中遍历来重建二叉树')
    root = A.reConstructBinaryTree(prelist, midlist)
    print(preOrder(root))
    


