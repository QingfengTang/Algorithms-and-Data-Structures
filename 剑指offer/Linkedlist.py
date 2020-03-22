
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

