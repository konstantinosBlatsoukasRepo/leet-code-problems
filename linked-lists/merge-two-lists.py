"""
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val > l2.val:
            newNode = ListNode(l2.val)
            newNode.next = self.mergeTwoLists(l1, l2.next)
        else:
            newNode = ListNode(l1.val)
            newNode.next = self.mergeTwoLists(l2, l1.next)

        return newNode
