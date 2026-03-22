# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prevNode = None
        while curNode is not None:
            duplicate = False
            while curNode.next is not None and curNode.next.val == curNode.val:
                duplicate = True
                curNode.next = curNode.next.next
            if duplicate:
                if prevNode is not None:
                    prevNode.next = curNode.next
                else:
                    head = curNode.next
            else:
                prevNode = curNode
            curNode = curNode.next

        return head
        