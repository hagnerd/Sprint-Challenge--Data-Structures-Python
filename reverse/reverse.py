class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    """ LinkedList """
    def __init__(self):
        """ init """
        # reference to the head of the list
        self.head = None

    def __str__(self):
        output = ""
        current_node = self.head

        if current_node is None:
            return output

        if current_node is not None:
            output += f"({current_node})"

        if current_node.next_node is not None:
            output += " -> "

        while current_node.next_node is not None:
            current_node = current_node.next_node
            output += f"({current_node})"
            if current_node.next_node is not None:
                output += f" -> "

        return output

    def add_to_head(self, value):
        """ add_to_head """
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        """ contains fn """
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()

        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        """ reverse_list """

        # if length <= 1 return early; nothing needs to happen
        if self.head is None or self.head.next_node is None:
            return

        prev_node = None
        next_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node

            prev_node = current_node
            current_node = next_node

        self.head = prev_node

