'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
note：给出的所有元素都大于0，若数组大小为0，请返回0。

非递减 a[i-1] <= a[i]    非递增 a[i-1] >= a[i]
递减 a[i-1] > a[i]       递增 a[i-1] < a[i]
'''

def minNumberInRotateArray(rotateArray):
    if not len(rotateArray):
        return 0
    i = len(rotateArray) - 1
    
    while i:
        if rotateArray[i] < rotateArray[i-1]:
            return rotateArray[i]
        
        i -= 1
    

if __name__ == '__main__':
    # origin array [2,3]
    rotateArray = [3,2]
    result = minNumberInRotateArray(rotateArray)
    print(result)


