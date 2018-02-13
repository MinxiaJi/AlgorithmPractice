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


# stack
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head = None):
        self.head = head
    
    def append(self,new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            return False
        
    def delete(self):
        if self.head:
            h = self.head
            self.head = self.head.next
            return h.value
        else:
            return False

class stack(object):
    def __init__(self,f = None):
        self.ll = LinkedList(f)
        
    def push(self,new_element):
        self.ll.append(new_element)
        
    def pop(self):
        return self.ll.delete()
    
    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

stack = stack(e1)

stack.pop()