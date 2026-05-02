# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input: ListNode in a LinkedList
        # output ListNode in a LinkedList
        # approach: two pointers, use the left pointer + 1 difference to set next to next.next
        # add an extra left dummy and manipulate anything after
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n-= 1
        while right:
            right = right.next
            left = left.next
        if left.next:
            left.next = left.next.next
        else:
            left.next = None
        return dummy.next

