class Node:

    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None 

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def AtBegining(self,newdata):
        newNode = Node(newdata)
        newNode.nextval = self.headval
        self.headval = newNode

    def AtEnd(self,newdata):
        newNode = Node(newdata)
        if self.headval is None:
            ##empty Linked list
            self.headval = newNode
            return
        last = self.headval
        while last.nextval :
            last = last.nextval
        
        last.nextval = newNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("middlwNode is absent")
            return 
        newNode = Node(newdata)
        newNode.nextval = middle_node.nextval
        middle_node.nextval = newNode

    def RemoveNode(self,key):
        temp = self.headval
                
        ## if the head node is going to get deleted
        if (temp.dataval == key):
            self.headval = temp.nextval 
            temp = None 
            return

        
        ## search
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next
        ## if the key match while loops break and we get the previous
        ## node in prev variable
        while (temp is not None):
            if temp.dataval == key:
                break
            prev = temp 
            temp = temp.nextval
        

        ## if nothing matches
        if (temp == None):
            return

        prev.nextval = temp.nextval

        temp=None 
        


        

                




list1 = SLinkedList()
list1.headval = Node("MON")
e2 = Node("Tue")
e3 = Node("Fri")

list1.headval.nextval = e2
e2.nextval = e3 

list1.AtBegining("SAT")
list1.AtEnd("END")
list1.Inbetween(e3,"MiDDLE")
list1.RemoveNode("SAT")

list1.listprint()



