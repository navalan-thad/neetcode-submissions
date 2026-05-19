# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(node):
            if not node:
                return [None]
            frontier = deque([node])
            path = [node.val]

            while frontier:
                curr = frontier.popleft()
                children = [curr.left, curr.right]

                for i in children:
                    if i:
                        path.append(i.val)
                        frontier.append(i)
                    else:
                        path.append(None)
            return path

        return bfs(p) == bfs(q)
