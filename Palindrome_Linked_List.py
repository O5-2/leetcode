# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        list1 = []
        cur = head
        while cur is not None:
            list1.append(cur.val)
            cur = cur.next
        low = 0
        high = len(list1)-1
        while low < high:
            if list1[low] != list1[high]:
                return False
            low += 1
            high -= 1
        return True
