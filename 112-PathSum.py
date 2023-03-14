class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return targetSum - root.val == 0
        else:
            need = targetSum - root.val
            return self.hasPathSum(root.left, need) or self.hasPathSum(root.right, need)
