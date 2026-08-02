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

        temp= head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        middle = count // 2
        temp = head
        for i in range(middle):
            temp = temp.next
        return temp
        
        





       
    
    
        
        