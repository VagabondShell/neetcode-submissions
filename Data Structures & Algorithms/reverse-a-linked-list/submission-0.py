# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #to swap two elemets next should be pointing to the prevouse one 
        #and the the previouse should point to the next
        prev = None 
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev