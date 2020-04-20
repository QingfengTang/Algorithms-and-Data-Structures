
class ListNode():
    '''
    定义链表节点
    '''
    def __init__(self, x):
        self.val = x
        self.next = None
    
class LinkList():
    def __init__(self):
        self.head = None
    
    def initList(self, data):
        # 创建头节点
        self.head = ListNode(data[0])
        point = self.head
        # 初始化其他节点
        for i in data[1:]:
            node = ListNode(i)
            point.next = node
            point = node
        
        return self.head
    
    def PrintList(self, head):
        list_bak = []
        if head == None:
            return []
        else:
            node = head
            while node != None:
                list_bak.append(node.val)
                node = node.next
        
        return list_bak

    def reverseLinked(self, head):
        '''
        反转单向链表
        1.定义p,q节点来实现节点的单个反转
        2.定义r节点来保存还未反转的其他节点
        3.通过p,q一步一步依次反转遍历一遍链表后全部反转完毕
        '''
        if head == None:
            return None
        
        p = head
        q = head.next
        # 链表反转后p.next指向None
        p.next = None

        while q:
            # r来保存q.next的值防止提前覆盖，也是提供了还为反转节点的地址
            r = q.next
            # 反转p,q节点
            q.next = p
            # p,q节点向前移动一位        
            p = q
            q = r
        
        return p
    
    def FindKthToTail(self, head, k):
        '''
        输入一个链表，输出该链表中倒数第k个结点
        solution1:遍历整个链表，知道链表的长度n，如果n>k则返回正数第n-k个节点
        solution2:采用两个指针，一个快指针，一个慢指针，让快指针先向前移动K个节点后，
                  再同时移动两个指针，当快指针遍历结束时，慢指针所在的位置就是倒数第K个节点
        '''
        fast_node = head
        slow_node = head

        while k:
            # 当k大于链表的长度时退出
            if not fast_node:
                return None
            fast_node = fast_node.next
            k -= 1
        
        while fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
        
        return slow_node
            



        



if __name__ == '__main__':
    linkedList = LinkList()
    data = [1, 22, 5, 6, 8, 2,9, 5]
    head = linkedList.initList(data)

    linked = linkedList.PrintList(head)
    print(linked)
    #链表反转
    reversed_head = linkedList.reverseLinked(head)
    linked = linkedList.PrintList(reversed_head)
    print(linked)

