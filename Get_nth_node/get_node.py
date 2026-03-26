from preloaded import Node

def get_nth(node, index):
    if index < 0:
        raise Exception("Invalid index")
    current = node
    counter = 0
    while current:
        if counter == index:
            return current
        current = current.next
        counter += 1
    raise Exception("Index out of bounds")