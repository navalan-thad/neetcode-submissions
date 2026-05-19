# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        frontier = deque([root])

        while frontier:
            curr = frontier.popleft()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                children = [curr.left, curr.right]
                for child in children:
                    if child:
                        frontier.append(child)

        return root
        
