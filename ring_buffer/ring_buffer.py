from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if capacity has not not reached max
        if len(self.storage) < self.capacity:
            #if current node is empty 
            if not self.current:
                #assign head node to current, this will be the oldest node
                self.current =  self.storage.head
            #add item to tail
            self.storage.add_to_tail(item)
        #if capacity has reached max
        else:
            #assign item to current node
            self.current.value = item
            #update current node to be next node which is the next oldest node
            self.current = self.current.next
            #if current node is None
            if not self.current:
                #assign head node to current
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #c is head node
        c = self.storage.head
        #iterate until node is None
        while c:
            #append node value to buffer array
            list_buffer_contents.append(c.value)
            #assing next node to c 
            c = c.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
