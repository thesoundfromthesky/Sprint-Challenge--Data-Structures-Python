from q import Queue
from s import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
               self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        
        else:
            if self.right:
               self.right.insert(value)
            else:
               self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        queue = Queue()
        queue.enqueue(self)

        while queue.len():
            node = queue.dequeue()
            if node.value == target:
                return True
            elif node.value < target:
                if node.right:
                     queue.enqueue(node.right)
            else:
                if node.left:
                     queue.enqueue(node.left)
        
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        stack = Stack()
        stack.push(self)
        while stack.len():
            node = stack.pop()
            if not node.right:
                return node.value
            elif node.value <= node.right.value:
                stack.push(node.right)
            
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        
        while queue.len():              

            n = queue.dequeue()            
            print(n.value)

            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)

      
 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(self)

        while s.len():
            n = s.pop()
            print(n.value)

            if n.left:
                s.push(n.left)
            if n.right:
                s.push(n.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)