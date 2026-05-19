# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        frontier = deque([root])
        all_levels = []

        while frontier:

            size = len(frontier)
            level = []
            for _ in range(size):
                curr = frontier.popleft()
                if curr:
                    level.append(curr.val)

                    for child in [curr.left, curr.right]:
                        if child:
                            frontier.append(child)

            all_levels.append(level)

        return all_levels if all_levels != [[]] else []


        