'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''

class Power():
    def solution1(self, base, exponent):
        '''
        采用二进制的思路 3^5=3^0101=3^0100 * 3^0001 = 3^4 * 3^1
        通过例子可以发现 可以根据exponent的二进制码中1所在位置的权重去计算次方
        3^0100  中根据8421可以发现1所在位置权重为4，即3^4, 每向右移动一位权重变为原来的平方，所以base *= base
        '''
        if not base:
            return False
        
        if not exponent:
            return 1
        
        result = 1
        exp = exponent
        # 只考虑指数是正数的情况，负指数将其变成倒数就OK
        if exp < 0:
            exp = abs(exp)
        while exp:
            if exp&1 == 1:
                result *= base
            
            base *= base
            exp = exp>>1
        
        if exponent < 0:
            return 1/result
        else:
            return result
    
    def solution2(self, base, exponent):
        '''
        考虑各种情况，利用循环迭代计算次方
        '''
        if not base:
            return False
        
        if not exponent:
            return 1
        
        exp = abs(exponent)
        result = 1
        while exp:
            result *= base
            exp -= 1
        
        if exponent < 0:
            return 1/result
        else:
            return result


if __name__ == '__main__':
    p = Power()
    print(p.solution2(2,-3))