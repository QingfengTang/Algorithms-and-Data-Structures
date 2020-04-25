'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
'''

class Solution():
    def __init__(self):
        self.stack = []
        self.minElementStack = []
    
    def push(self, node):
        if not len(self.stack):
            # 空栈
            self.minElementStack.append(node)
        else:
            if node < self.minElementStack[-1]:
                self.minElementStack.append(node)
            
        
        self.stack.append(node)

    def pop(self):
        if self.stack:
            node = self.stack.pop()
            if node == self.minElementStack[-1]:
                self.minElementStack.pop()
            return node
        

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.stack:
            return self.minElementStack[-1]

if __name__ == '__main__':
    stack = Solution()
    stack.push(3)
    print(stack.min())
    stack.push(4)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(3)
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.push(0)
    print(stack.min())