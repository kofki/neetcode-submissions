# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1
        ptr = head
        index = length -n -1
        i = 0
        if length == n:
            return head.next
        while ptr and ptr.next:
            if index == i:
                a = ptr.next
                ptr.next = ptr.next.next
                break
            else:
                i+= 1
                ptr = ptr.next
        return head