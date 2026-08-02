# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # traverse full linked list, count all nodes
        # take one temp and traverse linked list and count nodes
        # find the midlle,count // 2 
        # then traverse to middle node 

        """temp= head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        middle = count // 2
        temp = head
        for i in range(middle):
            temp = temp.next
        return temp"""

        # slow and fast pointer
        #move slow 1 step and fast 2 steps
        #if fast reaches end of the list then slow at the middle
        #return slow => middle of the list

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        
        





       
    
    
        
        