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

def MidOrderByNonRecursion(root):
    '''
    非递归实现 中序遍历
    '''
    node = root
    stack = []
    while node or len(stack)!=0:
        while node:
            stack.append(node)
            node = node.left
        
        if len(stack)!=0:
            node = stack.pop()
            print(node.data, end=' ')
            node = node.right

def PreOrderByNonRecursion(root):
    '''
    非递归实现前序遍历
    '''
    node = root
    stack = []
    while node or len(stack)!=0:
        while node:
            stack.append(node)
            print(node.data, end=' ')
            node = node.left
        
        if len(stack)!=0:
            node = stack.pop()
            node = node.right

def BacOrderNonRecursion(root):
    '''
    非递归 后序遍历
    '''
    node = root
    stack = []
    temp = TreeNode(None)
    while node or len(stack)!=0:
        while node:
            stack.append(node)
            node = node.left
        if len(stack)!=0:
            node = stack.pop()
            if not node.right or node.right==temp:
                print(node.data, end=' ')
                temp = node
                node = None
            else:
                stack.append(node)
                node = node.right
                
def LevelTraversal(root):
    '''
    层次遍历(level traversal)
    '''
    queue = [root]

    while queue:
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        node = queue.pop(0)
        print(node.data, end=' ')


def PrintLeaves(root):
    '''
    输出树的叶节点
    '''
    if root:
        if not root.left and not root.right:
            print(root.data, end=' ')
        PrintLeaves(root.left)
        PrintLeaves(root.right)

def BackTreeDepth(root):
    '''
    求树的深度  后序遍历 max(numleft, numright) + 1
    '''
    if not root:
        return 0
    left = BackTreeDepth(root.left)
    right = BackTreeDepth(root.right)
    return  max(left, right) + 1

def LevelTraversalTreeDepth(root):
    '''
    层序遍历求树深度,每遍历一层深度加一
    '''
    queue = [root]
    depth = 0
    while queue:
        current_node = len(queue)
        # 每一层的所有结点退出结束后深度加一
        while current_node:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
            current_node -= 1
        
        depth += 1
    
    return depth


    

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
        要想通过两种遍历来恢复出二叉树，其中必须含有中序遍历
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
    print('非递归中序遍历')
    MidOrderByNonRecursion(A)
    print('\n非递归前序遍历')
    PreOrderByNonRecursion(A)
    print('\n非递归后序遍历')
    BacOrderNonRecursion(A)
    print('\n层次遍历')
    LevelTraversal(A)
    print('\n打印叶节点')
    PrintLeaves(A)
    print('\n后序遍历求树深度')
    print(BackTreeDepth(A))
    print('\n层序遍历求树深度')
    print(LevelTraversalTreeDepth(A))



