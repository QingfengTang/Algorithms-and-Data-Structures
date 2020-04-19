'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

note:  正数的 原码=反码=补码
       负数的反码  除符号位以外各位取反,   负数的补码即 反码加1
       对于二进制数n, n&(n-1)则消去了n最右边的一个1
'''

def numberof1(n):
    count = 0
    # python中 bin(-3)= -0b11 得到的依然是正数的码值，但是机器对于负数是用补码来表示的
    # 所以用n&0xffffffff得到python下n的补码，当然看起来依然是正数的样子
    if n < 0:
        n = n&0xffffffff
    
    while n:
        count += 1
        n = n&(n-1)
    '''
    # 另一种解法
    while n:
        count += (n&1)
        n = n>>1
    '''
    
    return count


if __name__ == '__main__':
    print(numberof1(-3))