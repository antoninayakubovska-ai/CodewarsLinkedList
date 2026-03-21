from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return

    parts = list_repr.split(' -> ')
    parts.pop()
    reversed_parts = parts[::-1]
    currNode = None

    for value in reversed_parts:
        currNode = Node(int(value), currNode)

    return currNode
