'''
栈 先进后出
队列 先进先出
都可以用list的append和pop方法来实现
'''
class Stack():
    '''
    采用列表的方式实现
    '''
    def __init__(self):
        self.stack = []

    def push(self, value):
        # 入栈
        self.stack.append(value)

    def pop(self):
        # 出栈
        if self.stack == []:
            raise LookupError('stack is empty!')
        else:
            # pop会改变栈，如果只是查看可用self.stack[-1]
            return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)




class LinkNode():
    '''
    链表节点
    '''
    def __init__(self, val):
        self.val = val
        self.next = None

class Head():
    '''
    队列指针
    '''
    def __init__(self):
        # 指向队列头
        self.left = None
        # 指向队列尾
        self.right = None

class Queue():
    '''
    采用单向链表实现
    '''
    def __init__(self):
        # 初始化队列头尾指针
        self.head = Head()

    def enQueue(self, value):
        # 入队
        node = LinkNode(value)
        # 非空队列
        if self.head.right:     
            # 更新链表最后指向
            self.head.right.next = node
            # 更新队列指针指向
            self.head.right = node

        else:
            # 空队列
            self.head.left = node
            self.head.right = node
    

    def deQueue(self):
        # 队列中只有一个元素
        if self.head.left and self.head.left == self.head.right:
            node = self.head.left
            # 当队列为空时将队列指针变为None
            self.head.left = None
            self.head.right = None
            return node.val
        # 队列中不止一个元素
        elif self.head.left and self.head.left != self.head.right:
            node = self.head.left
            self.head.left = self.head.left.next
            return node.val
        # 队列中没有元素
        else:
            raise LookupError('Queue is empty')
        
    def is_empty(self):
        if self.head.right:
            return False
        else:
            return True

    def show_queue(self):
        if self.head.right:
            queue = []
            node = self.head.left
            while node:
                queue.append(node.val)
                node = node.next
            
            return queue
        else:
            return False


class SimulatedQueue():
    '''
    用两个栈来模拟一个队列
    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, value):
        self.stack1.append(value)

    def pop(self):

        if self.stack2 == []:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            
            return self.stack2.pop()
        
        else:
            return self.stack2.pop()
            


class SimulatedStack():
    '''
    两个队列模拟一个栈
    '''
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def enQueue(self, value):
        self.queue1.append(value)
    
    def deQueue(self):
        if len(self.queue1) == 1:
            return self.queue1.pop()
        else:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))

            node = self.queue1.pop()
            while len(self.queue2):
                self.queue1.append(self.queue2.pop(0))
            
            return node



if __name__=='__main__':

    new_stack = Stack()
    print(new_stack.is_empty())
    new_stack.push(6)
    new_stack.push(3)
    print(new_stack.stack)
    print(new_stack.is_empty())
    new_stack.pop()
    print(new_stack.stack)
    new_stack.pop()
    print(new_stack.stack)
    print(new_stack.is_empty())
    
    print('*****')
    queue = Queue()
    print(queue.is_empty())
    print(queue.show_queue())
    queue.enQueue(5)
    queue.enQueue(8)
    print(queue.is_empty())
    print(queue.show_queue())
    queue.deQueue()
    print(queue.show_queue()) 
    queue.deQueue()
    print(queue.show_queue())
    print(queue.is_empty())
    print('队列模拟栈')
    stack = SimulatedStack()
    stack.enQueue(2)
    stack.enQueue(3)
    print(stack.deQueue()) 
