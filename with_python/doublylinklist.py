class None:
    ''' Node class For the doubly Linked List '''
    def __init__(self,data=None,prev=none,next=None):
        self.data = data
        self.prev = prev 
        self.next = next

    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList:

    def __init__(self):
        self.head = Node()

    def append(self,data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node

    def preappend(self,data):
        first_node = self.head.next
        new_node = Node(data,Node,first_node)
        self.head.next = new_node
        if first_node:
            first_node.prev = new_node

    
    def search(self,item):
        current_node = self.node.next
        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next

    def remove_node(self,node):

        ''' fullly understand
        you have to make change in
        the previous node
        and the next node both
        to remove a doubly link list
        
        '''
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next 
        if node.next:
            node.next.prev = node.prev





    def remove(self,item):
        node = self.search(item)
        if node==None:
            return
        self.remove_node(node)

