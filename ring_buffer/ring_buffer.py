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
        self.capacity = capacity
        #current will be index 0
        self.current = 0
        #use python array instead of doubly linked list
        self.storage = [None] * self.capacity 

    def append(self, item):
        #assign item to current array
        self.storage[self.current]= item
        #increment current index by 1 which is the next oldest index
        self.current += 1
        #if current index has reached capacity            
        if self.current >= self.capacity:
            #assign 0 to current
            self.current = 0

    def get(self):
     # Note:  This is the only [] allowed
     list_buffer_contents = [] 
     # TODO: Your code here
     #assign self storage to list buffer
     for i in self.storage:
         #if i exists
         if i:
             list_buffer_contents.append(i) 
     return list_buffer_contents

#advantage of using array over ddl
#fast random access compared to ddl
#disadvnatage of using array over ddl
#slow to insert an element to middle of array
#slow to increase size of array