# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def maxHeight(root):

            if not root:
                return 0
            left, right = 0, 0

            if root.left:
                left = maxHeight(root.left) + 1
            if root.right:
                right = maxHeight(root.right) + 1

            self.diameter = max(self.diameter, left+right)
        
            return max(left, right)

        maxHeight(root)

        return self.diameter
        