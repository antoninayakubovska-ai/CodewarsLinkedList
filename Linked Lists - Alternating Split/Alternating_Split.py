class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("Can`t be empty")

    first_head = head
    second_head = head.next

    currNode1 = first_head
    currNode2 = second_head

    while currNode2 is not None and currNode2.next is not None:
        currNode1.next = currNode2.next
        currNode1 = currNode1.next

        currNode2.next = currNode1.next
        currNode2 = currNode2.next

    currNode1.next = None
    return Context(first_head, second_head)
        