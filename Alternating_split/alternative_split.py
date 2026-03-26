class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes")
    first_head = head
    second_head = head.next
    curr1 = first_head
    curr2 = second_head
    while curr2 and curr2.next:
        curr1.next = curr2.next
        curr1 = curr1.next
        
        curr2.next = curr1.next
        curr2 = curr2.next
    curr1.next = None
    
    return Context(first_head, second_head)