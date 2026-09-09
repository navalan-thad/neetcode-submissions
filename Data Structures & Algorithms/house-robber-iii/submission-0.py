# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}

        def dp(node, canRob):
            if not node:
                return 0
            if (node, canRob) in memo:
                return memo[(node, canRob)]

            if canRob:
                left_rob = dp(node.left, False)
                right_rob = dp(node.right, False)
                rob = left_rob + right_rob + node.val
            else:
                rob = 0

            left_no_rob = dp(node.left, True)
            right_no_rob = dp(node.right, True)
            no_rob = left_no_rob + right_no_rob

            memo[(node, canRob)] = max(rob, no_rob)
            return memo[(node, canRob)] 

        return dp(root, True)
            

        
        