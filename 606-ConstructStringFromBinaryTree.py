class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root.left and not root.right:
            return str(root.val)

        left, right = "", ""
        if not root.right:
            left = "(" + self.tree2str(root.left) + ")"
        elif not root.left:
            right = "()" + "(" + self.tree2str(root.right) + ")"
        else:
            left = "(" + self.tree2str(root.left) + ")"
            right = "(" + self.tree2str(root.right) + ")"

        return str(root.val) + left + right
