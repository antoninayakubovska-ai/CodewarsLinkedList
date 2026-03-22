# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = head.next

        currNode = head
        prevNode = None
        while currNode is not None and currNode.next is not None:
            first = currNode
            second = currNode.next

            first.next = second.next
            second.next = first

            if prevNode:
                prevNode.next = second

            currNode = first.next
            prevNode = first

        return new_head
            