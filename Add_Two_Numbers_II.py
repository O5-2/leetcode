# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        num1 = str(cur1.val)
        num2 = str(cur2.val)
        while cur1.next != None:
            cur1 = cur1.next
            num1 += str(cur1.val)
        while cur2.next != None:
            cur2 = cur2.next
            num2 += str(cur2.val)
        ans = str(int(num1)+int(num2))
        ansNode = ListNode(int(ans[0]))
        cur = ansNode
        for i in range(1, len(ans)):
            cur.next = ListNode(int(ans[i]))
            cur = cur.next
        return ansNode
