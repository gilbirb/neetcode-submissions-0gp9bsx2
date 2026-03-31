# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(cur, prev):
            if not cur:
                return None
            if cur.next == None:
                cur.next = prev
                return cur
            
            a = rec(cur.next, cur)

            cur.next = prev
            return a
        
        return rec(head, None)