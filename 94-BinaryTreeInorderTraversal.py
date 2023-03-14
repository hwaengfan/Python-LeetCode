class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if root:
                nonlocal res
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res
