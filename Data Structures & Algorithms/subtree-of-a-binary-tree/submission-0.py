# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:   

    def isEqual(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and not node2 or node2 and not node1:
            return False

        if node1.val != node2.val:
            return False

        return self.isEqual(node1.left, node2.left) and self.isEqual(node1.right, node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        frontier = deque([root])
        while frontier:
            curr = frontier.popleft()
            if self.isEqual(curr, subRoot):
                return True
            
            children = [child for child in [curr.left, curr.right] if child]
            frontier += children

        return False


        