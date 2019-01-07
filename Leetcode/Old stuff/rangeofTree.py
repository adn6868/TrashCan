# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        STACK =[root]
        ans = 0
        good = range(L,R+1)
        while len(STACK) != 0:
            cur = STACK.pop(0)
            if cur.val in good:
                ans += cur.val
            STACK.append(self.left)
            STACK.append(self.right)
            
        return ans