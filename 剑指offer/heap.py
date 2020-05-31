'''
堆(heap)是一种完全二叉树，指除了最后一层之外，其他所有层的节点都是满的，而最后一层的节点都是靠左边
最大堆: 对于任意一个父结点，其子结点的值都小于这个父结点
最小堆: 对于任意一个父结点，其子结点的值都大于这个父结点

由于堆是完全二叉树，因此用数组来表示堆结构，而不是树，此时有下列结论:
对于任意一个父结点的序号n(数组的索引,从0开始)来说，它的子结点的序号一定是2n+1(左结点)和2n+2(右结点) 
!!! 有些叶子结点并没有子结点所以他们的2n+1必然是大于数组的长度的
同理，对于任意一个子结点n，其父结点的序号是floor((n-1)/2) == (n-1) // 2
!!! 当n=0时其没有父结点所以parent_index>=0
'''

class MinHeap():
    '''
    最小堆
    '''
    def __init__(self, array):
        self.array = array
        # 将array构建为最小堆
        for i in range((len(array)-1-1)//2, -1, -1):
            self.Sink(self.array, i)
    
    def Insert(self, num):
        '''
        以最小堆为例:
        1.将num插入到堆尾
        2.将num和其相对应的父结点相比较，如果num小于父结点则互换，直到父结点小于num
        相当于向上冒泡
        '''
        self.array.append(num)
        index = len(self.array)-1
        parent_index = (index-1) // 2
        while parent_index >= 0 and self.array[parent_index] > num:
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            '''
            if parent_index < 0:
                break
            '''
            index = parent_index
            parent_index = (index-1)//2
        
    def Sink(self, array, index):
        '''
        按照堆的性质，重排
        '''
        left_index = 2*index+1
        right_index = 2*index+2
        if left_index < len(array):
            left_val = array[left_index]
            # 左结点恰好为最后一个堆元素
            if right_index >= len(array):
                min_val = left_val
                min_index = left_index
            else:
                right_val = array[right_index]
                if right_val > left_val:
                    min_val = left_val
                    min_index = left_index
                else:
                    min_val = right_val
                    min_index = right_index
            # 将父结点与其最小的子结点交换
            if array[index] > min_val:
                array[index], array[min_index] = min_val, array[index]
            self.Sink(array, min_index)
            # 采用深拷贝，即地址指向不变
            self.array[:] = array

    
    def Pop(self):
        '''
        删除堆顶的元素，然后将最后一个堆元素放在堆顶，最后根据堆的性质下沉重排
        '''
        end_val = self.array.pop()
        min_val = self.array[0]
        self.array[0] = end_val
        self.Sink(self.array, 0)
        return min_val



class MaxHeap():
    '''
    最大堆
    '''
    def PerDown(self, array, index):
        '''
        最大堆重排
        '''
        parent = index
        size = len(array)-1
        x = array[parent]
        while 2*parent+1 <= size:
            child = parent*2+1
            if child!=size and array[child]<array[child+1]:
                child += 1
            if x >= array[child]:
                parent = child
                break
            else:
                array[parent] = array[child]
                array[child] = x
                parent = child
            


    def CreatMaxHeap(self, array):
        '''
        创建最大堆 先按照完全二叉树放在数组中，然后根据堆的特性来重排
        '''
        size = len(array)-1
        # 自底向上重排
        for i in range((size-1)//2,-1, -1):
            self.PerDown(array, i)

    def Insert(self, array, x):
        '''
        直接插入到堆的最后一个元素，然后自底向上按照堆的结构进行调整
        '''
        array.append(x)
        size = len(array) - 1
        # 从最后一个父结点开始，如果父结点的值小于x则将父结点的值下移
        while array[(size-1)//2] < x and size>0:
            array[size] = array[(size-1)//2]
            size = (size-1)//2
        # x小于此时的父结点，那么这时的size就是x所对应的位置
        array[size] = x
       
    def Delete(self, array):
        '''
        出堆顶
        将堆顶取出，然后把堆的最后一个元素放到堆顶，然后自顶向下安装堆的要求进行判断重排
        '''
        # 
        max_value = array[0]
        end_value = array.pop()
        array[0] = end_value
        # 自顶向下按照最大堆的结构重排
        size = len(array)-1
        parent = 0
        x = array[0]
        while 2*parent+1<=size:
            child = 2*parent+1
            # 判断是左节点值大还是右节点值大
            if child!=size and array[child] < array[child+1]:
                child += 1
            # 父结点大于子结点不交换否则就交换
            if  x >= array[child]:
                parent = child
                break
            else:
                array[parent] = array[child]
                array[child] = x

            parent = child
        
        return max_value
        
    

if __name__ == '__main__':
    a = [0,6,3,2,4,1]
    print('最小堆')
    minh = MinHeap(a)
    print(minh.array)
    minh.Insert(2)
    minh.Insert(7)
    print(minh.array)
    print(minh.Pop())
    print(minh.array)
    print('最大堆')
    b = [0,6,3,2,4,1,7]
    maxh = MaxHeap()
    maxh.CreatMaxHeap(b)
    print(b)
    maxh.Insert(b,9)
    print(b)
    print(maxh.Delete(b))
    print(b)



