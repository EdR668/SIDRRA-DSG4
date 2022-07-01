from Model.Node import node

class pila:
    def __init__(self):
        self.head=None
    def push(self,data):
        nodo=node(data)
        if self.head==None:
            self.head=nodo
        else:
            nodo.next=self.head
            self.head=nodo
    def pop(self):
        temp=self.head.next
        l=self.head
        self.head.next=None
        self.head=temp
        return l
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def longitud(self):
        temp=self.head
        contador=0
        while temp!=None:
            temp=temp.next
            contador+=1
        return contador
    def get(self,data):
        temp=self.head
        while temp!=None:
            if temp.data==data:
                break
            else:
                temp=temp.next
        return temp.data
    def getByIndex(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp  