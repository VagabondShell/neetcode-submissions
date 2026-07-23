# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        half = slow.next
        prev = slow.next = None
        while half:
            temp = half.next
            half.next = prev
            prev = half
            half = temp

        first = head
        while prev:
            temp1, temp2 = first.next, prev.next
            first.next = prev
            prev.next = temp1
            first, prev = temp1, temp2
