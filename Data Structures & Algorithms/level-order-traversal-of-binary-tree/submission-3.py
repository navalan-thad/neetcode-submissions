# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        if not root:
            return res

        q = deque([root])
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
            res.append(level)

        return res

