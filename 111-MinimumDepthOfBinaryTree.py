class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float('inf')

        def preorder(root, height):
            if not root:
                return
            elif not root.left and not root.right:
                nonlocal res
                res = min(res, height)
            else:
                preorder(root.left, height + 1)
                preorder(root.right, height + 1)

        preorder(root, 1)
        return res
