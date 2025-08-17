## INSERT AT BEGGINIG:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insertAtBeggning(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
## INSERT AT END:

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
## INSERT AT POSITION:

    
    def insrtAtPosition(self,data,index):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            for i in range(1,index):
                val = temp
                temp = temp.next
            val.next = node
            node.next = temp
## DELETE AT BEGGNING:

    def deleteAtBeggning(self):
        if self.head == None:
            return
        else:
            val = self.head.next
            self.head.next = None
            self.head = val
            
## DELETE AT END:

    def deleteAtEnd(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while(temp.next != None):
                val = temp
                temp = temp.next
            val.next = None
## DELETE AT POSITION:

    def deleteAtposition(self,index):
        if self.head == None:
            return
        else:
            temp = self.head
            priv = self.head
            for i in range(1,index):
                priv = temp
                temp = temp.next
            priv.next = temp.next
            temp.next = None
## PRINT DETAILS:
    def printdetails(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next

list1 = linkedList()
list2 = linkedList()
list3 = linkedList()
list1.insertAtBeggning(200)
list1.insertAtBeggning(300)
list1.insertAtBeggning(400)
list1.insertAtBeggning(500)
list1.insertAtBeggning(600)
list1.insertAtEnd(100)
list1.insrtAtPosition(1000,2)
list1.deleteAtBeggning()
list1.deleteAtEnd()
list1.deleteAtposition(3)
list1.printdetails()
