# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None or head.next.next is None:return False
        tmp=head.next.next
        
        while tmp and tmp.next:
            if head==tmp:
                return True
            head=head.next
            tmp=tmp.next.next
        return False
