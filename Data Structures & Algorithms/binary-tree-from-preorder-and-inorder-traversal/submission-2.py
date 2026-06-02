# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapping = {inorder[i]:i for i in range(len(inorder))}

        self.preorder_ind = 0

        def build(left, right):
            if left > right:
                return
            
            root_val = preorder[self.preorder_ind]
            self.preorder_ind += 1
            node = TreeNode(root_val)

            pivot = mapping[root_val]

            node.left = build(left, pivot-1)
            node.right = build(pivot+1, right)

            return node

        return build(0, len(inorder)-1)

        
        