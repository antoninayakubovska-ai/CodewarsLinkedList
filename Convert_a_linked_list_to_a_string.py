def stringify(node):
    result = []
    currNode = node

    while currNode is not None:
        result.append(str(currNode.data))
        currNode = currNode.next

    result.append('None')

    return ' -> '.join(result)
