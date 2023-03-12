class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def traverse(root):
            if not root:
                return [True, 0]
            left, right = traverse(root.left), traverse(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return traverse(root)[0]
