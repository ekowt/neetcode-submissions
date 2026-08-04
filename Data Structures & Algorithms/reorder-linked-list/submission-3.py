# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast =  head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
           
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
      
        l1 = head
        l2 = prev
        while l1 and l2:
            tmp1,tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l2 = tmp2
            l1 = tmp1
      
        