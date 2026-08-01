# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # reached meeting point 
                slow = head # reset the slow's position to start while keeping the fast at meeting point 
                while slow != fast:
                    #now both are moving at same speed
                    slow = slow.next
                    fast = fast.next
                
                return slow #or fast as both are point the same spot
        return None
    

       