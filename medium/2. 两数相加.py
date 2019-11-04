# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp_l1 = l1
        tmp_l2 = l2
        int_l1 = ''
        int_l2 = ''
        while tmp_l1.next:
            int_l1 = str(tmp_l1.next) + int_l1
        while tmp_l2.next:
            int_l2 = str(tmp_l2.next) + int_l2
        tmp_str = str(int(int_l1) + int(int_l2))[::-1]
        result = ListNode(tmp_str[0])


        tmp_node = None
        for i in range(1, len(tmp_str)):
            tmp_node = ListNode()
            result

        list_node = ListNode(2)
        list_node.next = ListNode(4)
        list_node.next.next = ListNode(3)


if __name__ == '__main__':
    list_node = ListNode(2)
    list_node.next = ListNode(4)
    list_node.next.next = ListNode(3)

    list_node = ListNode(5)
    list_node.next = ListNode(6)
    list_node.next.next = ListNode(4)
