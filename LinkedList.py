
# coding: utf-8

# In[ ]:

class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class Linkedlist(object):
    def __init__(self,head = None):
        self.head = head
    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

def question5(ll,m):
    count = 1
    current = ll
    while current.next:
        current = current.next
        count+=1
    len_ll = count
    position = len_ll-m
    if position < 0:
        return 'Out of boundary'
    else:
        count_ = 0
        current_ = ll
        while count_ < position:
            current_ = current_.next
            count_+=1
        return current_.data

n1 = Node(1)
n2 = Node('a')
n3 = Node(3)
n4 = Node(0.5)


ll = Linkedlist(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

