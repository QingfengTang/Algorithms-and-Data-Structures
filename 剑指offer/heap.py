'''
堆(heap)是一种完全二叉树，指除了最后一层之外，其他所有层的节点都是满的，而最后一层的节点都是靠左边
最大堆: 对于任意一个父结点，其子结点的值都小于这个父结点
最小堆: 对于任意一个父结点，其子结点的值都大于这个父结点

由于堆是完全二叉树，因此用数组来表示堆结构，而不是树，此时有下列结论:
对于任意一个父结点的序号n(数组的索引)来说，它的子结点的序号一定是2n+1(左结点)和2n+2(右结点) 
!!! 有些叶子结点并没有子结点所以他们的2n+1必然是大于数组的长度的
同理，对于任意一个子结点n，其父结点的序号是floor((n-1)/2) == (n-1) // 2
!!! 当n=0时其没有父结点所以parent_index>=0
'''

class Heap():
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
        

    

if __name__ == '__main__':
    a = [0,1,3,2,4,6,7,8,9,5,10]
    h = Heap(a)
    print(h.array)
    h.Insert(2)
    h.Insert(6)
    print(h.array)
    print(h.Pop())
    print(h.array)



