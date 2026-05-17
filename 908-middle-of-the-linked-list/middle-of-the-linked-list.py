# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):

        '''
        #brute force
        length = 0
        temp = head
        while temp:
            length = length + 1
            temp = temp.next
        middle = length // 2
        temp = head
        for i in range(middle):
            temp = temp.next
        return temp
       '''
        # slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
       
    
    
        
        