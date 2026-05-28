# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        rs = []

        frontier = deque([root])

        while frontier:
            for i in range(len(frontier)):
                curr = frontier.popleft()
                if curr:
                    if i == 0:
                        rs.append(curr.val)
                    for child in [curr.right, curr.left]:
                        if child:
                            frontier.append(child)
        return rs

            



            
        