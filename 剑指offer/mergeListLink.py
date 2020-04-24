'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Merge():
    def soluton1(self, pHead1, pHead2):
        '''
        非递归实现：从头开始逐次比较，将小拿出来排好，再移位，重复操作直到最后
        '''
        tmp = ListNode(0)
        pHead = tmp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tmp.next = pHead1
                # phead1位置更新为下一位
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        if not pHead1:
            tmp.next = pHead2
        if not pHead2:
            tmp.next = pHead1
        return pHead.next

    def soluton2(self, pHead1, pHead2):
        '''
        递归实现
        '''
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val > pHead2.val:
            pHead2.next = self.soluton2(pHead1, pHead2.next)
            return pHead2
        else:
            pHead1.next = self.soluton2(pHead1.next, pHead2)
            return pHead1            

        
