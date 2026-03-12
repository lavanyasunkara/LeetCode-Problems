# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        x=head
        z=None
        length=0
        while x:
            length=length+1
            x=x.next
        pos=length-n+1
        if pos == 1:
            return head.next
        x=head
        for _ in range(pos-1):
            z=x
            x=x.next
            
        z.next=x.next


        return head
        

        