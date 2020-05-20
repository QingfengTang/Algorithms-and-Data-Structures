'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''

class SumOfMaxSubArray():
    def FindGreatestSumOfSubArray(self, array):
        '''
        O(n^2)
        '''
        if len(array) == 0:
            return None
        max_subseq_sum = array[0]
        for j in range(len(array)):
            sum_subseq = 0
            for i in range(j, len(array)):
                sum_subseq += array[i]
                if sum_subseq > max_subseq_sum:
                    max_subseq_sum = sum_subseq
        
        return max_subseq_sum
    
    def FindMaxSubarraySum(self, array):
        '''
        一个序列的最大连续子列和可以看作为当前的值array[i]和之前序列的最大连续子列和temp_subarray_sum构成的，所以只需要分析之前的最大连续子列和的变化即可
        temp_subarray_sum>=0 时可以直接加上array[i]
        temp_subarray_sum<0 时，若array[i]>=0则此时的最大子列就是array[i],故有temp_subarray_sum=array[i]
                                若array[i]<0，如果加上array[i]必不是最大子列，而最大子列要求连续，故将之前的最大子列放弃，将array[i]作为最大子列开始
        O(n)
        '''
        if len(array)==0:
            return None
        max_subarray_sum = array[0]
        temp_subarray_sum = array[0]
        for i in range(1, len(array)):
            if temp_subarray_sum >= 0:
                temp_subarray_sum += array[i]
            else:
                temp_subarray_sum = array[i]
            
            if temp_subarray_sum > max_subarray_sum:
                max_subarray_sum = temp_subarray_sum
        
        return max_subarray_sum
    


if __name__ == '__main__':
    a = SumOfMaxSubArray()
    list1 = [6, -3, -2, 7, -15, 1, 2, 2]
    list2 = [1, -2, 3, 10, -4, 7, 2, -5]
    print(a.FindGreatestSumOfSubArray(list2))
