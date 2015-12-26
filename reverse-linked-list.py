# Reverse a singly linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        first = True
        next = head.next
        while next is not None:
            tmp = next.next
            next.next = head
            if first:
                head.next = None
                head = next
                first = False
            else:
                head = next
            next = tmp
        return head
