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
    1-2-3 单链表反转
    :param head:
    :return:
    """
    prev = None
    # head头是1
    curr = head

    while curr != None:
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
    两个有序的链表合并
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    i_list = []
    while head:
        i_list.append(head)
        head = head.next
    i_list[-n - 1].next = i_list[-n + 1]


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
    print(tmp)
    tmp = hasCycle(three)
    print(tmp)
    mergeTwoLists(three,three1)
