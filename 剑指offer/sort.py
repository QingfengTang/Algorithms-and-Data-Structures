'''
将一组数按照大小排序
!!!note:当列表作为参数在函数间传递时，对列表的修改要注意深浅拷贝
例如 对于列表array 在函数中进行array[i]=value 这种修改时为深拷贝，会对原来的array进行修改
     而对于array=[value]时为浅拷贝，这是array的变化不会影响原来的array
'''

class Sort():
    # array一维列表
    def BubbleSort(self, array):
        '''
        冒泡排序  时间复杂度O(n^2)
        1.将a[j]和a[j+1]比较大的放后面，依次遍历一遍，大的数就在尾端冒泡
        2.由于每次遍历大的数已经放好，所以对末尾已经排号的就不再排序
        '''
        for i in range(len(array)):
            # 每排一次需要一次循环
            for j in range(len(array)-i-1):
                # 此处-i是因为对已经排好的就不再动了
                # -1是由于采用了array[j+1]防止越界
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        
        return array
    
    def CountingSort(self, array):
        '''
        计数排序 桶排序的最简单形式 O(n+k) k为桶的个数或者最大值
        1.根据array的值域设置桶的个数并初始化，要求每一个桶内只有一个元素
        2.按照桶统计array中的元素出现的次数
        3.按照桶的顺序和元素出现的次数输出
        '''
        result = []
        # 根据array的值域来设定桶数
        buckets = [0 for i in range(10)]
        
        # 装桶，统计频率
        '''
        # 有更简单的写法
        for i in range(len(array)):
            for j in range(len(buckets)):
                if array[i] == j:
                    buckets[j] += 1
        '''
        for i in array:
            buckets[i] += 1

        
        # 按照桶的顺序输出元素
        for i in range(len(buckets)):
            while buckets[i] > 0:
                result.append(i)
                buckets[i] -= 1
        
        return result


            


    def BucketSort(self, array):
        '''
        桶排序
        '''
        return array
    def QuickSortMain(self, array):
        '''
        快排序 分而治之的递归排序
        1.在array中确定一个基准base，一般为首元素 
        2.先从右往左移动即array[j]>base，否则 将小于base的array[j]赋给array[i],此时array[i]原来的值并没有消失而是在base中
        3.从左往右移动即array[i]<base，否则将大于base的array[i]给array[j],此时array[j]在1中已经移动了，所以不存在消失问题
        4.当左右两个指针相遇时将base放在此时的位置，这时base的左边小于base右边大于base
        5.同理递归左边序列和右边序列
        '''
        low = 0
        high = len(array) - 1
        result = self.QuickSortFunc(array, low, high)
        return result

    def QuickSortFunc(self, array, low, high):
        i = low
        j = high

        if i < j:
            # 定义基准值
            temp = array[i]
            # 当左右指针相遇时退出
            while i != j:
                
                # 由于基准值选的是array[i]所以先从右往左
                # 从右往左，将大于等于base的放在右
                while j>i and array[j]>=temp:
                    j -= 1
                array[i] = array[j]
                
                # 从左往右
                while j>i and array[i]<temp:
                    i += 1
                array[j] = array[i]
                
            # 将基准值放在左右指针相遇处
            array[i] = temp

            self.QuickSortFunc(array, low, i-1)
            self.QuickSortFunc(array, i+1, high)
              
        return array
                
    def HeapSort(self, array):
        '''
        堆排序
        '''
        if not array:
            return None
        # 构建最大堆
        for i in range((len(array)-1-1)//2, -1, -1):
            self.CreateMaxHeap(array, i, len(array))
        
        #
        for i in range((len(array)-1), 0, -1):
            temp = array[0]
            array[0] = array[i]
            array[i] = temp
            self.CreateMaxHeap(array, 0, i) 
        

        return array

    def CreateMaxHeap(self, array, index, length):
        '''
        创建最大堆
        '''
        left_index = 2*index+1
        right_index = 2*index+2
        if left_index < length:
            left_val = array[left_index]
            if right_index >= length:
                max_index = left_index
                max_val = left_val
            else:
                right_val = array[right_index]
                if left_val > right_val:
                    max_index = left_index
                    max_val = left_val
                else:
                    max_index = right_index
                    max_val = right_val
            
            if array[index] < max_val:
                array[index], array[max_index] = array[max_index], array[index]
            self.CreateMaxHeap(array, max_index, length)
            return array
        


    
    def MergeSort(self, array):
        '''
        并归排序 NlogN
        1.采用分而治之的策略，将array不断的二分一直到一个元素
        2.合并，依次比较left和right的大小，并移动值小的指针
        '''
        if len(array) <= 1:
            return array
        
        middle = len(array) // 2
        left = self.MergeSort(array[:middle])
        right = self.MergeSort(array[middle:])

        return self.MergeFun(left, right)
    
    def MergeFun(self, left, right):
        '''
        并归排序的 合并部分
        '''
        temp = []
        lpoint = 0
        rpoint = 0
        while lpoint < len(left) and rpoint < len(right):
            if left[lpoint] < right[rpoint]:
                temp.append(left[lpoint])
                lpoint += 1
            else:
                temp.append(right[rpoint])
                rpoint += 1

        if lpoint == len(left):
            temp += right[rpoint:]
        else:
            temp += left[lpoint:]

        return temp 





if __name__ == '__main__':
    array = [2,5,3,8,5,7,4,9]
    solution = Sort()
    result = solution.HeapSort(array)
    print(result)


