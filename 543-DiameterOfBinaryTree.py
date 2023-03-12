class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def traverse(root):
            nonlocal maxDiameter
            if not root:
                return 0
            left, right = traverse(root.left), traverse(root.right)
            maxDiameter = max(maxDiameter, left + right)
            return 1 + max(left, right)

        traverse(root)
        return maxDiameter
