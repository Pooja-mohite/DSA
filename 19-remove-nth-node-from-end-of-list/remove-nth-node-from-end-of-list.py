# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # brute force
         
        length = 0
        temp = head
        while temp:
            length = length + 1
            temp = temp.next
        if length ==n:
            return head.next
        temp = head
        for i in range(length-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
            