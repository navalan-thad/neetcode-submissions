# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        order = []

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                children = [curr.left, curr.right]

                for child in children:
                    if child:
                        queue.append(child)
            order.append(level)

        return order





        