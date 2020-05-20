'''
二分查找(Binary Search)
二分查找必须为有序数组
'''
def BinarySearch(array, k):
    '''
    array 非递减 O(logN)
    '''
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < k:
            # note! 这里mid必须要加一或者减一，
            # 例如 left=8, right=9,则mid=8,如果此时left=mid，那么会造成死循环
            left = mid+1 
        elif array[mid] > k:
            right = mid-1
        else:
            return True
    
    return False
        




if __name__ == '__main__':
    array = [1,2,3,4,5,6,6,8]
    print(BinarySearch(array, 4))


