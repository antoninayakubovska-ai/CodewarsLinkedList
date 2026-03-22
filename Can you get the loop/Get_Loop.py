def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    currNode = slow.next

    while slow!=currNode:
        currNode = currNode.next
        count += 1

    return count
