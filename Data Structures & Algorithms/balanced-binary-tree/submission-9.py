# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(node):
            if not node:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)
            if left == -1 or right == -1:
                return -1
            else:
                left, right = left+1, right+1
            if abs(left - right) <= 1:
                return max(left, right)
            return -1

        if root:
            val = getHeight(root)
            if val == -1:
                return False
        return True





        