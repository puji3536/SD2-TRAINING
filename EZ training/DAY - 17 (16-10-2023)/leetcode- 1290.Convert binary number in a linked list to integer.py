#1290. Convert binary number in a linked list to integer
class Solution(object):
    def getDecimalValue(self, head):
        s=""
        curr=head
        while(curr):
            s+=str(curr.val)
            curr=curr.next
        return int(s,2)