from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = self.storage.head
        if self.current:
            print(self.current.value, item)
        if self.capacity == len(self.storage) and self.current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next
        elif self.capacity == len(self.storage) and self.current == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.capacity == len(self.storage):
            self.current.insert_after(item)
            self.storage.length += 1
            temp = self.current.next.next
            self.storage.delete(self.current)
            self.current = temp
        else:
            print("hit", item, len(self.storage))
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        temp = self.storage.head
        list_buffer_contents.append(temp.value)
        while temp != self.storage.tail:​
            temp = temp.next
            if self.storage.length == 5:
                print("asdfasdfsafasdf", self.storage.head.value, self.storage.head.next.value,
                      self.storage.head.next.next.value, self.storage.head.next.next.next.value, self.storage.head.next.next.next.next.value)
​
            list_buffer_contents.append(temp.value)

         return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
