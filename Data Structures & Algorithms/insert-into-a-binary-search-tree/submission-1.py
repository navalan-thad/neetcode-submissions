# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new = TreeNode(val)
        if not root:
            return new

        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = new
                    return root
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = new
                    return root
                else:
                    curr = curr.right

        