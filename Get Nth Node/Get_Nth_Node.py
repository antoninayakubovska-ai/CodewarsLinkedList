from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None or index<0:
        raise Exception('The list is empty or the index < 0')

    currNode = node
    currIndex = 0

    while currNode is not None:
        if currIndex == index:
            return currNode
        currNode = currNode.next
        currIndex += 1
    raise Exception("Index > length")
