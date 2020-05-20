class Solution:
    def Permutation(self, ss):
        # write code here
        length = len(ss)
        if length <= 1:
            return ss
        lists = []
        for i in range(length):
            first_str = ss[i]
            # 这里的ss[:i]+ss[i+1:] 刚好把ss[i]扣出来
            for temp_sub_list in self.Permutation(ss[:i]+ss[i+1:]):
                temp = first_str + temp_sub_list
                if temp not in lists:
                    lists.append(temp)
        return sorted(lists)

if __name__ == '__main__':
    a = Solution()
    print(a.Permutation('acb'))
