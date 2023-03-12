class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def preorder(root1, root2):
            if not root1 and not root2:
                return None
            elif not root1:
                return root2
            elif not root2:
                return root1
            else:
                root = TreeNode(root1.val + root2.val)
                root.left = preorder(root1.left, root2.left)
                root.right = preorder(root1.right, root2.right)
                return root

        return preorder(root1, root2)
