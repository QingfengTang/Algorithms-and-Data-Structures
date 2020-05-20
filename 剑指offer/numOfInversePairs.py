'''
'''
class Solution:
    def InversePairs(self, data):
        # write code here
        return self.MergeSort(data)
    
    def MergeSort(self, data):
        if len(data) <= 1:
            return data, 0
        middle = len(data)//2
        left, num_left = self.MergeSort(data[:middle])
        right, num_right = self.MergeSort(data[middle:])
        
        temp, num_merge = self.Merge(left, right)
        nums = num_left + num_right + num_merge
        return temp, nums
    
    
    def Merge(self, left, right):
        temp = []
        lpoint = 0
        rpoint = 0
        numofinversepairs = 0
        while lpoint < len(left) and rpoint < len(right):
            if left[lpoint] > right[rpoint]:
                temp.append(right[rpoint])
                rpoint += 1
                numofinversepairs += (len(left)-lpoint)
            else:
                temp.append(left[lpoint])
                lpoint += 1
        
        if lpoint == len(left):
            temp += right[rpoint:]
        else:
            temp += left[lpoint:]
        
        return temp, numofinversepairs

if __name__ == '__main__':
    a = Solution()
    r = a.InversePairs([1,2,3,4,5,6,7,0])
    print(r)
