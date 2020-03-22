'''
斐波拉契数列
0 1 1 2 3 5 8 13 21 34
f(n) = f(n-1) + f(n-2)

要求输入一个整数n，请你输出斐波那契数列的第n项(从0开始，第0项为0),n<=39
'''
class Fibonacci():
    def Solution1(self, n):
        '''
        斐波拉契数列的n项是n-1和n-2项之和
        所以将n-1和n-2在计算的时候保存下来就可用避免反复的递归运算
        '''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            f1 = 0
            f2 = 1
            for i in range(n):
                f = f1 + f2
                f2 = f1
                f1 = f
            return f
    
    def Solution2(self, n):
        '''

        '''
        g = 0
        f = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1

        while n>1:
            f += g
            g = f - g 
            n -= 1
        
        return f



if __name__ == '__main__':
    result = Fibonacci().Solution2(9)
    print(result)


