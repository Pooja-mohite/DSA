# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        values =[]
        temp = list1
        while temp:
            values.append(temp.val)
            temp = temp.next
        temp = list2
        while temp:
            values.append(temp.val)
            temp = temp.next
        values.sort()
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next









