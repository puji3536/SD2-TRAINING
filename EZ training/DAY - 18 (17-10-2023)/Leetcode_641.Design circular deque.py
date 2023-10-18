class MyCircularDeque:

    def __init__(self, k):
       self. dq=[]
       self.k=k
       

    def insertFront(self, value):
        if len(self.dq)<self.k:
            self.dq=[value]+self.dq
            return True
        return False

    def insertLast(self, value):
        if len(self.dq)<self.k:
            self.dq.append(value)
            return True
        return False

    def deleteFront(self):
        if len(self.dq)>0:
            self.dq.pop(0)
            return True
        return False

    def deleteLast(self):
        if len(self.dq)>0:
            self.dq.pop()
            return True
        return False

    def getFront(self):
        if len(self.dq)>0:
            return self.dq[0]
        return -1

    def getRear(self):
        if len(self.dq)>0:
            return self.dq[-1]
        return -1

    def isEmpty(self):
        if not self.dq:
            return True
        return False

    def isFull(self):
        if len(self.dq)==self.k:
            return True
        return False