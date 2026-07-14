# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=l1
        ll1=[]
        ll2=[]
        while current:
            a=current.val
            current=current.next
            ll1.append(a)
        current=l2
        while current:
            a=current.val
            current=current.next
            ll2.append(a)
        n1=n2=0
        print(ll1,ll2)
        for i in range(len(ll1)):
            n1=n1+ll1[i]*10**i
        for i in range(len(ll2)):
           n2=n2+ll2[i]*10**i
        sum=n1+n2
        sum=str(sum)
        lis=list(sum)
        print(lis)
        liss=[]
        for i in lis:
            new=int(i)
            liss.append(new)
        liss.reverse()
        d=ListNode(0)
        current=d
        for num in liss:
            current.next=ListNode(num)
            current=current.next
        return d.next

