class node:
  def __init__(self,data):
      self.data=data
      self.next=None


class pila:
    def __init__(self):
        self.head=None
        self.longitud=0
    def stack(self,data):
        nodo=node(data)
        if self.head==None:
            self.head=nodo
        else:
            nodo.next=self.head
            self.head=nodo
        self.longitud+=1
    def pop(self):
        if self.head!=None:
            temp=self.head.next
            l=self.head
            self.head.next=None
            self.head=temp
            self.longitud-=1
            return l
        else:
            return None
    def printList(self):
        cadena=""
        temp=self.head
        contador=1
        contador2=0
        while temp!=None:
            if contador2<self.longitud-1:
                cadena+=temp.data+" , "
                temp=temp.next
                contador2+=1
            if contador2==self.longitud-1:
                cadena+=temp.data
                temp=temp.next

            if (len(cadena)+41)>60*contador:
                cadena+="\n"
                contador+=1

        return cadena

    def printList2(self):
        cadena=""
        temp=self.head
        contador=1
        contador2=0
        for i in range(10):
            if contador2<self.longitud-1:
                cadena+=temp.data+" , "
                temp=temp.next
                contador2+=1
            if contador2==self.longitud-1:
                cadena+=temp.data
                temp=temp.next

            if (len(cadena)+41)>60*contador:
                cadena+="\n"
                contador+=1

        return cadena

class cola:
    def __init__(self):
        self.head=None
        self.longitud=0
    def queue(self,data):
        nodo=node(data)
        if self.head==None:
            self.head=nodo
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=nodo
        self.longitud+=1

    def dequeue(self):
        if self.head!=None:
            antefinal=self.head
            if antefinal.next==None:
                self.head=None
                self.longitud-=1
                return antefinal
            else:
                while antefinal.next.next!=None:
                    antefinal=antefinal.next
                temp=antefinal.next
                antefinal.next=None
                self.longitud-=1
                return temp
        else:
            return None

    def printList(self):
        cadena=""
        temp=self.head
        contador=1
        contador2=0
        while temp!=None:
            if contador2<self.longitud-1:
                cadena+=temp.data+" , "
                temp=temp.next
                contador2+=1
            if contador2==self.longitud-1:
                cadena+=temp.data
                temp=temp.next

            if (len(cadena)+41)>60*contador:
                cadena+="\n"
                contador+=1

        return cadena

    def printList2(self):
        cadena=""
        temp=self.head
        contador=1
        contador2=0
        for i in range(10):
            if contador2<self.longitud-1:
                cadena+=temp.data+" , "
                temp=temp.next
                contador2+=1
            if contador2==self.longitud-1:
                cadena+=temp.data
                temp=temp.next

            if (len(cadena)+41)>60*contador:
                cadena+="\n"
                contador+=1

        return cadena
