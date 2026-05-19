# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        curr = root
        visited = []
        frontier = []
        last_visited = None

        while curr or frontier:
            while curr:
                frontier.append(curr)  
                curr = curr.left

            node = frontier[-1]

            if node.right and last_visited != node.right:
                curr = node.right
            else:
                visited.append(node.val)
                last_visited = frontier.pop()
            

        return visited



        