from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

            if self.current is None or self.current.next is None:
                self.current = self.storage.head

            return

        removed = self.storage.remove_node_from_head()
        self.storage.add_to_tail(item)

        if removed == self.current:
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        storage_len = len(self.storage)
        current_node = self.current

        if current_node is None:
            list_buffer_contents.append(None)
        else:
            list_buffer_contents.append(current_node.value)

        should_bail = current_node is None
        capacity = storage_len if storage_len < self.capacity else self.capacity

        while len(list_buffer_contents) < capacity and not should_bail:
            # 1) current_node is not None and current_node.next is not None
            # 2) make current_node self.storage.head
            if current_node is not None and current_node.next is not None:
                current_node = current_node.next
                list_buffer_contents.append(current_node.value)
            else:
                current_node = self.storage.head
                list_buffer_contents.append(current_node.value)


        return [value for value in list_buffer_contents if value is not None]

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
