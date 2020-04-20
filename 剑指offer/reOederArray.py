'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

'''

def reOrderArray1(array):
        '''
        以空间换时间
        '''
        tempArray = []
        head = 0
        for i in array:
            # 偶数从尾部插入
            if i%2==0:
                tempArray.append(i)                
            else:
                # 奇数从头插入
                tempArray.insert(0, i)
                head += 1
        # 此时奇数部分为原来相对位置的反序，而偶数部分依然保持相对位置不变
        temp = tempArray[:head][::-1]
        # 这里有个坑: python中extend, append都是对原来list的修改,所以并没有返回值
        # 所以 直接 return temp.extend(tempArray[head:])会返回None,因为没有返回值
        temp.extend(tempArray[head:])
        return temp


def reOrderArray2(array):
    '''
    借助于冒泡排序的思路，前偶后奇就换
    '''
    for i in range(len(array)):
        # 在内循环时和冒泡就不一样了，循环次数不用减去i，因为循环一次并不能保证最后一位就是正确的
        # 例如 list尾部为双奇数
        for j in range(len(array)-1):
            if array[j]%2==0 and array[j+1]%2==1:
                temp = array[j]
                array[j] = array[j+1]
                a[j+1] = temp
    
    return array






if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,7]
    print(reOrderArray2(a))