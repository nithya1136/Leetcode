# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return None
            l1, l2 = head, head
            prev = None  
            while l2 and l2.next:
                prev = l1
                l1 = l1.next
                l2 = l2.next.next
            prev.next = l1.next  
            return head
                