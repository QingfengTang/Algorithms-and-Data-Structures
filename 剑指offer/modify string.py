'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
'''

class Solution1():
    # s源字符串
    def ReplaceSpace(self, s):
        string = ''
        for i in s:
            if i == ' ':
                string += '%20'
            else:
                string += i
        
        return string


class Solution2():
    def ReplaceSpace(self, s):
        return s.replace(' ', '%20')


if __name__ == '__main__':
    s = 'We are happy'
    solution = Solution2()
    result = solution.ReplaceSpace(s)
    print(result)
