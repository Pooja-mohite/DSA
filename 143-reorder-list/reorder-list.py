# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        #brute force
        """
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        i =0
        j = len(nodes)-1
        while i < j:
            nodes[i].next = nodes[j]
            i = i+1
            if i == j:
                break
            nodes[j].next = nodes[i]
            j = j-1
        nodes[i].next = None
        """
        # (slow -fast)
        if not head:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow.next
        slow.next = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            #merge 
        first = head
        second = prev
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

