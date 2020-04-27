'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
'''
class Solution:
    def __init__(self):
        self.stack = []
    
    def isPopOrder(self, pushV, popV):
        '''
        新建一个栈，按照A的入栈顺序入栈，在入栈后判断栈顶的元素是否和出栈的元素相等，如果相等则都执行一次pop
        如果B是A的出栈顺序，那么最后按照B的顺序出栈，A必为空栈
        '''
        if not pushV or not popV:
            return False
        
        for i in pushV:
            self.stack.append(i)
            if self.stack.append == popV[0]:
                self.stack.pop()
                popV.pop(0)

        for i in range(len(self.stack)):
            if self.stack[-1] == popV[0]:
                self.stack.pop()
                popV.pop(0)
        
        if self.stack:
            return False
        else:
            return True
    
    def optimizeIsPopOrder(self, pushV, popV):
        '''
        这是对isPopOrder的优化版本
        '''
        
        while popV:
            if self.stack and self.stack[-1] == popV[0]:
                self.stack.pop()
                popV.pop(0)
            elif pushV:
                self.stack.append(pushV.pop(0))
            else:
                return False

        return True 