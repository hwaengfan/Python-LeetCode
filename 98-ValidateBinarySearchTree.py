class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(root, low, high):
            if not root:
                return True
            elif root.val < high and root.val > low:
                return isBST(root.left, low, root.val) and isBST(root.right, root.val, high)
            else:
                return False

        return isBST(root, float("-inf"), float("inf"))
