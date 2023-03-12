class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        target = set()

        def levelorder(root):
            if root:
                nonlocal target
                if root.val in target:
                    return True
                target.add(k - root.val)
                return levelorder(root.left) or levelorder(root.right)

        return levelorder(root)
