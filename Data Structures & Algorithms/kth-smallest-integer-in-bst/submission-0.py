# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from math import inf

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        maxHeap = []

        def dfs(node):
            if not node:
                return
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, -node.val)
            else:
                if -node.val > maxHeap[0]:
                    heapq.heappushpop(maxHeap, -node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(maxHeap)
        return maxHeap[0] * -1
        