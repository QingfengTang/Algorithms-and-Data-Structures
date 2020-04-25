'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution():
    def PrintMatrix(self, matrix):
        '''
        1.通过分析可以发现在顺时针打印矩阵时，每一圈开始的位置是矩阵的对角线，坐标为[start, start]
        2.每打印一圈，col和row都要减去二，此时考虑到start是从零开始的，因此如果还可以继续打印新的一圈则必须满足col>2*start and row>2*start
        3.无论是怎样的矩阵从左到右的这一步是必有的
        4.只要当前这一圈的矩阵行数大于start则必然可以从上到下打印
        5.要满足当前这一圈，从右到左，则必须满足当前矩阵的行数和列数 都大于 start
        6.要在当前这一圈有从下到上，则必须当前这一圈的行数大于start+1并且当前这一圈的列数要大于start
        '''
        col = len(matrix[0])
        row = len(matrix)
        # 每一圈的起始位置
        start = 0
        clockwise_matrix = []
        
        while col > 2*start and row > 2*start:
            # 更新当前圈的行数和列数
            end_row = row - start - 1
            end_col = col - start - 1
            # 从左到右，是必有的
            # range是左闭右开区间，由于之前已经减过1了，所以在这里要加一
            for i in range(start, end_col+1):
                clockwise_matrix.append(matrix[start][i])
            # 从上到下
            if end_row > start:
                for i in range(start+1, end_row+1):
                    clockwise_matrix.append(matrix[i][end_col])
            # 从右到左
            if end_col > start and  end_row > start:
                for i in reversed(range(start, end_col)):
                    clockwise_matrix.append(matrix[end_row][i])
            # 从上到下
            if end_row > start+1 and end_col > start:
                for i in reversed(range(start+1, end_row)):
                    clockwise_matrix.append(matrix[i][start])
            
            start += 1
        
        return clockwise_matrix
            
