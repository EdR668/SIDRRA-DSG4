from Model.Node import node
class list:
    def __init__(self):
        self.head=None
    def queue(self,data):
        nodo=node(data)
        if self.head==None:
            self.head=nodo
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=nodo
    def dequeue(self):
        final=self.head
        if final.next==None:
            self.head=None
            return final
        else:
            while final.next.next!=None:
                final=final.next
            temp=final.next
            final.next=None
            return temp
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
    def remove(self,data):
        temp=self.head
        if temp==None:
            pass
        else:
            if temp.data==data:
                if self.longitud()==1:
                    self.head=None
                else:
                    self.head=self.head.next
                    temp.next=None
            else:
                while temp.next!= None:
                    if temp.next.data==data:
                        break
                    else:
                        temp=temp.next

                if temp.next.next==None:
                    temp.next=None
                else:
                    temp2=temp.next

                    temp.next=temp.next.next
                    temp2.next=None
    def getByIndex(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp