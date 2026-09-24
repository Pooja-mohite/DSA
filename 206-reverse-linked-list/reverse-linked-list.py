# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        #Brute force
        # take one empty list, and store the head in temp variable, then while temp != null, add data in empty list...then reverse that list and return head
        """emplist = []
        temp = head
        while temp:
            emplist.append(temp.val)
            temp = temp.next
        emplist.reverse()
        temp = head
        i = 0
        while temp:
            temp.val = emplist[i]
            i = i+1
            temp = temp.next
        return head"""

        # 3 pointers
        # save next node in nextnode and then reverse the currentnext 
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev



     
        