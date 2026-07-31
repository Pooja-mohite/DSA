# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # initialize current node as head, head means starting node
        # create hashset, check if current node in set or not 
        # if current node exist then yes cycle xists then return true else add in set
        # and update the current node as next node

        nodeset = set()
        currentnode = head
        if currentnode < 0:
            return False
        while currentnode:
            if currentnode in nodeset:
                return True
            else:
                nodeset.add(currentnode)
            currentnode = currentnode.next
        return False
        

        