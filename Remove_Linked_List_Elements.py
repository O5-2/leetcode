# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        cur = head.next
        last = head
        while cur is not None:
            if cur.val == val:
                last.next = cur.next
                cur = cur.next
            else:
                last = cur
                cur = cur.next
        return head
