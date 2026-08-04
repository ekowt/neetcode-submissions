# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second :
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        l1 = head
        while second:
            tmp1,tmp2 = l1.next,second.next
            l1.next = second
            second.next = tmp1
            second = tmp2
            l1 = tmp1

        
        