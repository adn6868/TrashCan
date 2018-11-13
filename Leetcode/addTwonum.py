# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value = l1.val + l2.val
        carry = value // 10
        value = value % 10
        ans = ListNode(value)

        while (l1.next != None or l2.next != None):
            if l1.next == None:
                l2 = l2.next
                value = l2.val + carry	
            elif l2.next == None:
                l1 = l1.next
                value = l1.val + carry
            else:
                l1 = l1.next
                l2 = l2.next
                value = l1.val + l2.val + carry

            carry = value // 10
            value = value % 10
            # E.write("Carry: "+ str(carry)+ '\n')
            # E.write("Value: "+ str(val)+ '\n')
            # E.write(str(val)+'\n')
            v = ListNode(value)
            ite = ans
            while ite.next != None:
                ite= ite.next
            ite.next = v		
            # E.write("Current Ans: "+ ans.toString()+ '\n')
        if carry!= 0:
            c = ListNode(carry)
            ite = ans
            while ite.next != None:
                ite= ite.next
            ite.next = c

        return ans