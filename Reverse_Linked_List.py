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
            return None
        if head.next is None:
            return head
        cur = head
        stack = []
        while cur.next is not None:
            stack.append(cur)
            cur = cur.next
        stack.append(cur)
        node = stack.pop()
        tail = node
        for i in range(len(stack), 0, -1):
            node.next = stack.pop()
            node = node.next
        node.next = None
        return tail
