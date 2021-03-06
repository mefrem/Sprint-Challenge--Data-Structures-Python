class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        self.next = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    # def reverse_list(self, node, prev):
    #     # You must use recursion for this solution
    #     if node == None:
    #         return node
    #     if node.next == None:
    #         return prev
    #     node_next = self.reverse_list(node.next, node)
    #     node.next.node = node
    #     node.next = None
    #     return node_next
    
    def reverse_list(self, item, tail = None):
        next_ = item.next
        item.next = tail
        if next_ is None:
            return item
        else:
            return self.reverse_list(next_, item)
