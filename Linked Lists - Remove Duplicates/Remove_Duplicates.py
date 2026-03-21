class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    currNode = head
    while currNode is not None and currNode.next is not None:
        if currNode.data == currNode.next.data:
            currNode.next = currNode.next.next
        else:
            currNode = currNode.next
    return head
