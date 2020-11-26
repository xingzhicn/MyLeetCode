# 单链表反转
# 链表中环的检测
# 两个有序的链表合并
# 删除链表倒数第 n 个结点
# 求链表的中间结点

class ListNode():
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node


def reverseList(head):
    """
    1-2-3
    :param head:
    :return:
    """
    prev = None
    # head头是1
    curr = head

    while curr != None:
        # 2的next指到临时变量上，然后转到1上
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev


def hasCycle(head):
    """
    给定一个链表，判断链表中是否有环。
    :type head: ListNode
    :rtype: bool
    """
    i_set = set()
    while head:
        if head not in i_set:
            return True
        i_set.add(head)
        head = head.next


def mergeTwoLists(l1, l2):
    """
    输入： l1 1->2->4  l2 1->3->4
    输出：1->1->2->3->4->4

    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return
    if l2 is None:
        return
    if l1.val>l2.val:
        # l1 1->2->4  l2 1->3->4




if __name__ == '__main__':
    # 链表初始化
    one = ListNode(3, None)
    two = ListNode(2, one)
    three = ListNode(1, two)

    # 链表初始化
    one1 = ListNode(3, None)
    two1 = ListNode(2, one1)
    three1 = ListNode(1, two1)

    tmp = reverseList(three)
    print()
