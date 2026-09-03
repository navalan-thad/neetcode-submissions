class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:

                curr = root.right
                while curr.left:
                    curr = curr.left
                
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)

            else:
                if root.left:
                    return root.left
                else:
                    return root.right

        return root

        