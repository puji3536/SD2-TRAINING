class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            curr.next=new
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=dll()
for i in l:
    o.insertatbeg(i)
    '''
    o.insertatend(i)
    '''
    '''
    o.deleteatbeg(i)
    '''
    '''
    o.deleteatend(i)
    '''
o.printing()