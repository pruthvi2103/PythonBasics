''' Singly Linked List Program  in python
The 2 classes are:
 Singly Linked List Node : Denotes each node of Linked List. 
 with objects:
    value : which is stored inside the node
    next : which is the pointer to next node

 Singly Linked List : Denotes  the actual Linked List with methods:
    getTail : which returns the tail of the LL
    display : Displays LL
    insertT : inserts element at Tail
    deleteT : delets tail
    
 '''

class SinglyLLNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLL():
    def __init__(self,value):
        self.head=SinglyLLNode(value)

    def getTail(self):
        n=self.head
        while n.next != None:
            n = n.next
        return n
    
    def display(self):
        
        n = self.head
        a=[]
        while n != None:
            a.append(n.value)
            n = n.next
        
        print(*a,sep=" -> ")
    
    def insertT(self,value):
        n = self.getTail()
        n.next=SinglyLLNode(value)

    def deleteT(self):
        n=self.head

        if n is None:
            print("Cant Delete Empty List")
            return

        elif n.next is None:
            del n
            return
        else:
            while n.next.next is not None:
                n = n.next
            del n.next.next
            n.next = None
# Driver

N = SinglyLL(100)

N.insertT(123)
N.insertT(1234)
N.display()
# OP : 100 -> 123 -> 1234
N.deleteT()

N.display()
# OP : 100 -> 123 
    
            

        