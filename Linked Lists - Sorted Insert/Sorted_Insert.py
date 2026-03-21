""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):

    dataNode = Node(data)
    if head is None or data <= head.data:
        dataNode.next = head
        return dataNode

    currNode = head

    while currNode.next is not None and currNode.next.data<data:
        currNode = currNode.next
    dataNode.next = currNode.next
    currNode.next = dataNode

    return head
