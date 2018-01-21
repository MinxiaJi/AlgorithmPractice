
# coding: utf-8

# Question 1

# In[12]:

def question1(s,t):
    if type(s) != str or type(t) != str:
        err_msg = 'Error: input should be strings!'
        return err_msg
    # s_list = sorted(s)
    t_list = sorted(t)
    
    for i in range(len(s)-len(t)+1):
        if sorted(s[i:i+len(t_list)]) == t_list:
            return True
    
    return False    


# In[13]:

# edge test case 1: empty string
print question1('','')
# should print True

# edge test case 2: input not string
print question1(12345, 32)
# should return error message, Error: input should be strings!

# test case 3: udacity example
print question1('udacity','ad')
# should print True

# test case 4
print question1('udacitttttttttty','tyi')
# should print Fasle


# Question 2

# In[29]:

def question2(a):
    
    if type(a) != str:
        err_msg = 'Error: input should be strings!'
        return err_msg
    
    if len(set(a)) == len(a):
        err_msg2 = 'Error: Doesn\'t exist palindromic substring contained in a!'
        return err_msg2
    
    # check every possible palindromic and remeber the index for head and tail, save them to a list
    longest = []
    for i,item in enumerate(a):
        current_letter = item
        following_str = a[i+1:]
        for j, letter in enumerate(following_str):
            if letter == current_letter:
                longest.append([j+i+1,i])
    # compute length of each possible palindromic and save it to a dictionary.
    # Key is length while value is index of head and tail
    index_longest = {}
    # find the maximum length and return its correspoinding index pair
    for k in longest:
        index_longest[k[0]-k[1]]=k
    head_tail = index_longest[max(index_longest)]
    head_index = head_tail[1]
    tail_index = head_tail[0]
    return a[head_index:tail_index+1]


# In[30]:

# edge test case 1: empty string
print question2('')
# should print error message 2: Doesn\'t exist palindromic substring contained in a!

# edge test case 2: no palindromic substring
print question2('abc')
# should print error message 2: Doesn\'t exist palindromic substring contained in a!

# test case 3
print question2('abba')
# should print abba

# test case 4
print question2('dabbacba')
# should print abbacba


# Question 3

# In[41]:

def question3(G):
    
    if type(G) != dict:
        return "Error: G is not dictionary!"
    
    ####
    # Clean overlaps and sort edges
    ####
    vertices = G.keys()
    edges = []
    for i in G:
        for j in G[i]:
            if i < j[0]:
                edges.append([j[1],i, j[0]])
            else:
                edges.append([j[1],j[0],i])

    edges_clean = []
    for i in edges:
        if not i in edges_clean:
            edges_clean.append(i)

    edges_clean = sorted(edges_clean)
    
    ####
    # Only keep useful edges: number of nodes -1 edges; Without cycle.
    ####
    edges_need = []
    vertices = [[i] for i in vertices]
    for i in edges_clean:
        for j in range(len(vertices)):
            if i[1] in vertices[j]:
                left = j
            if i[2] in vertices[j]:
                right = j
    
        if left < right:
            edges_need.append(i)
            vertices[left].append(vertices[right][0])
            vertices.pop(right)
        if left > right: 
            edges_need.append(i)
            vertices[right].append(vertices[left][0])
            vertices.pop(left)
        if len(vertices) == 1:
            break
    ####
    # Construct adjacency list
    ####    
    adj = {}
    
    for i in edges_need:

        if i[1] in adj and i[2] in adj:
            adj[i[1]].append((i[2],i[0]))
            adj[i[2]].append((i[1],i[0]))

        elif i[1] in adj and i[2] not in adj:
            adj[i[1]].append((i[2],i[0]))
            adj[i[2]] = [(i[1],i[0])]

        elif i[1] not in adj and i[2] in adj:
            adj[i[2]].append((i[1],i[0]))
            adj[i[1]] = [(i[2],i[0])]

        else:
            adj[i[1]] = [(i[2],i[0])]
            adj[i[2]] = [(i[1],i[0])]

        
    return adj


# In[42]:

# edge test case 1: empty graph
print question3({})
# should print empty dictionary

# edge test case 2: input is not a dictionary
print question3(['A:(B,2)','B:(A,2)'])
# should print error message: G is not dictionary!

# test case 3: udacity example
G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)], 
     'C': [('B', 5)]}
print question3(G)
# should print {'A': [('B', 2)],
#               'B': [('A', 2), ('C', 5)], 
#               'C': [('B', 5)]}

# test case 4
G = {'A': [('B', 7), ('D', 5)],

         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],

         'C': [('B', 8), ('E', 5)],

         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],

         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],

         'F': [('D', 6), ('E', 8), ('G', 11)],

         'G': [('E', 9), ('F', 11)]}
print question3(G)
# should print {'A': [('D', 5), ('B', 7)],
#               'B': [('A', 7), ('E', 7)],
#               'C': [('E', 5)],
#               'D': [('A', 5), ('F', 6)],
#               'E': [('C', 5), ('B', 7), ('G', 9)],
#               'F': [('D', 6)],
#               'G': [('E', 9)]}


# Question 4

# In[43]:

class Node(object):

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None

        

class BST(object):

    def __init__(self, root):

        self.root = Node(root)

        

    def build_tree(self, T):

        self.build_tree_helper(self.root, T)

        

    def build_tree_helper(self, start, T):

        index = start.value

        if sum(T[index]) > 0:

            for i, node in enumerate(T[index]):

                if node == 1:

                    if i < index:

                        start.left = Node(i)

                        self.build_tree_helper(start.left, T)

                    else:

                        start.right = Node(i)

                        self.build_tree_helper(start.right, T)

    

    def search(self, find_val):

        return self.BST_search(self.root, find_val)

        

    def BST_search(self, start, find_val):

        if start:

            if start.value == find_val:

                return True

            elif start.value < find_val:

                return self.BST_search(start.right, find_val)

            else:

                return self.BST_search(start.left, find_val)

            

        return False

    

    def LCA(self, n1, n2):


        return self.LCA_helper(self.root, n1, n2)

    

    def LCA_helper(self, start, n1, n2):

        

        if start:

            if start.value < n1 and start.value < n2:

                # if both n1 and n2 are greater than root, then LCA lies in left

                return self.LCA_helper(start.right, n1, n2)

            

            if start.value > n1 and start.value > n2:

                # if both n1 and n2 are smaller than root, then LCA lies in left

                return self.LCA_helper(start.left, n1, n2)

            

            return start.value

        

        return None

    

    

def question4(T, r, n1, n2):

    

    # build tree

    tree = BST(r)

    tree.build_tree(T)

    

    if tree.search(n1) and tree.search(n2):

        return tree.LCA(n1, n2)

    

    else:

        error = "Error: either n1 or n2 is not in the tree!"

        return error


# In[47]:

# edge test case 1: both nodes are root node
T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
print question4(T,3,3,3)
# should print 3

# edge test case 2: Node doesn't in BST
print question4(T,3,2,4)
# should print error message: either n1 or n2 is not in the tree!

# test case 3: udacity example
print question4(T,3,1,4)
# should print 3

# test case 4
T = [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
print question4(T, 6, 0, 4)
# should print 3


# Question 5

# In[50]:

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
    
    if type(ll) != Node:
        return 'Error: ll is not a Node!'
    
    count = 1
    current = ll
    while current.next:
        current = current.next
        count+=1
    len_ll = count
    position = len_ll-m
    if position < 0:
        return 'Error: Out of boundary!'
    else:
        count_ = 0
        current_ = ll
        while count_ < position:
            current_ = current_.next
            count_+=1
        return current_.data


# In[51]:

n1, n2, n3, n4 = Node(1), Node('a'), Node(3), Node(0.5)
ll = Linkedlist(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

# edge case: ll is not Node
print question5(1,2)
# should print error message: ll is not a Node!

# edage case: m > length of linked list
print question5(n1,10)
# should print error message: Out of boundary!

# test case
print question5(n1,3)
# should print 'a'

