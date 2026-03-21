class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise Exception('source can`t be empty')

    first_source = source
    new_source = source.next

    first_source.next = dest
    new_dest = first_source

    return Context(new_source, new_dest)
