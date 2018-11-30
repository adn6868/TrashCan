# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import sys
E = sys.stderr
def insert(head,value):
    while head.next != None:
        head = head.next
    head.next = ListNode(value)
    
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        empty = True
        for l in lists:
            if l is not None:
                empty = False
        if empty:
            return []
        minn = lists[0].val
        for l in lists:
            minn = min(minn,l.val)
        ans = []
        # for i in range(len(lists)):
        #     if minn == lists[i].val:
        #         lists[i] = lists[i].next
        
                
        while len(lists) != 0:
            for l in lists:
                if l == None:
                    # E.write("removed:")
                    # print("remove")
                    lists.remove(l)
            if len(lists) == 0:
                break
            minn = lists[0].val
            for l in lists:
                minn = min(minn,l.val)
            
            ans.append(minn)
            
            for i in range(len(lists)):
                if minn == lists[i].val:
                    lists[i] = lists[i].next
                    break
        return ans
        
        