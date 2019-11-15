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
        int_l1 = tmp_l1.val
        int_l2 = tmp_l2.val
        while tmp_l1.next:
            int_l1 = str(tmp_l1.next.val) + str(int_l1)
            tmp_l1 = tmp_l1.next
        while tmp_l2.next:
            int_l2 = str(tmp_l2.next.val) + str(int_l2)
            tmp_l2 = tmp_l2.next
        tmp_str = str(int(int_l1) + int(int_l2))[::-1]
        result = ListNode(int(tmp_str[0]))
        tmp_node = result
        for i in range(1, len(tmp_str)):
            tmp_node.next = ListNode(int(tmp_str[i]))
            tmp_node = tmp_node.next

        return result


if __name__ == '__main__':
    list_node = ListNode(2)
    list_node.next = ListNode(4)
    list_node.next.next = ListNode(3)

    list_node1 = ListNode(5)
    list_node1.next = ListNode(6)
    list_node1.next.next = ListNode(4)

    list_node2 = Solution().addTwoNumbers(list_node, list_node1)
    assert list_node2.val == 7
    assert list_node2.next.val == 0
    assert list_node2.next.next.val == 8

