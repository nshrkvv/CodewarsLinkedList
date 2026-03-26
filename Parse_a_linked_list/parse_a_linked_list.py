from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    elements = list_repr.split(" -> ")
    current_node = None
    for i in range(len(elements) - 2, -1, -1):
        current_node = Node(int(elements[i]), current_node)
        
    return current_node