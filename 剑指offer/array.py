'''
# 在一个二维数组中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution1:
    '''
    由于数组左小右大，因此先按行检索然后利用矩阵中线二分查找
    '''
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 空数组检查
        if array == [[]]:
            return False
        # 获取数组大小
        col_num = len(array[0])
        row_num = len(array)
        
        # target > max and target < min
        if target > array[row_num-1][col_num-1] and target < array[0][0]:
            return False
        # 按照行来检索，利用矩阵的中线来对分
        for i in range(0, row_num):
            if array[i][i] == target:
                return True
            if array[i][i] > target:
                for j in range(0, i):
                    if array[i][j] == target:
                        return True
            if array[i][i] < target:
                for j in range(i+1, col_num):
                    if array[i][i] == target:
                        return True

class Solution2:
    '''
    从左下角开始只向上移动行而遍历列???
    感觉和普通遍历在复杂度上没啥区别
    '''
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # get array shape
        # 空数组检查
        if array == [[]]:
            return False

        # range()为左闭右开区间
        row = len(array) - 1
        col = len(array[0])
          
        while row >= 0:
            if array[row][0] == target:
                return True
            # target可能在row行
            if array[row][0]<target:
                for i in range(1, col):
                    if array[row][i] == target:
                        print(array[row][i])
                        return True
                # target不在row行
                row -= 1
            # target小于array[row][0]
            else:
                row -= 1
                            
        return False

class Solution3:
    '''
    由于矩阵左小右大且上小下大，所以可以从左下角开始判断，行列同时移动
    array[row-1][j]大于所有j列左边的数(包括j列)
    所以当target>array[i][j]时可以采用列移动来缩减搜索范围
    同理，由于上小下大所以当array[i][j]>target时就要向上移动行， 
    '''
    def Find(self, target, array):
           
        row = len(array)
        col = len(array[0])

        i=row-1
        j=0

        while i>=0 and j<col:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        
        return False





if __name__ == "__main__":
    target = 22
    #array = [[12,22,42,56],[13,25,110,99],[14,26,120,121]]
    array = [[]]
    solution = Solution3()
    result = solution.Find(target=target, array=array)
    print(result)

