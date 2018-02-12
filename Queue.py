class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
 class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        
    def append(self,new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def delete(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = None
        return current  


 class Queue(object):
    def __init__(self,f = None):
        self.ll = LinkedList(f)
        
    def enque(self,new_element):
        self.ll.append(new_element)
    
    def deque(self):
        return self.ll.delete()

 # test
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

Queue = Queue(e1)

Queue.enque(e2)

Queue.deque().value