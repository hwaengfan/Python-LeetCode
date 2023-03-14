class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)

    def dfs(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        elif not leftRoot or not rightRoot:
            return False
        else:
            return (leftRoot.val == rightRoot.val and
                    self.dfs(leftRoot.left, rightRoot.right) and
                    self.dfs(leftRoot.right, rightRoot.left))
