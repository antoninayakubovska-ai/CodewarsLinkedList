from preloaded import Node

def swap_pairs(head):
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
