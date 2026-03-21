from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)

    return chained
