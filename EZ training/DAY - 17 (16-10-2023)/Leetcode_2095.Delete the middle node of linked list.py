class Solution(object):
    def deleteMiddle(self, head):
        newnode=ListNode()
        newnode.next=head
        slow=newnode
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return newnode.next