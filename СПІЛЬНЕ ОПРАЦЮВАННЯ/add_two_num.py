# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        prevNode = None
        curNode = result
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + carry
            curNode.val = value%10
            carry = value//10
            curNode.next = ListNode()
            prevNode = curNode
            curNode = curNode.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            value = l1.val+ carry
            curNode.val = value%10
            carry = value//10
            curNode.next = ListNode()
            prevNode = curNode
            curNode = curNode.next
            l1 = l1.next

        while l2 is not None:
            value = l2.val + carry
            curNode.val = value%10
            carry = value//10
            curNode.next = ListNode()
            prevNode = curNode
            curNode = curNode.next
            l2 = l2.next

        if carry != 0:
            curNode.val = carry
        elif prevNode is not None:
            prevNode.next = None

        return result
