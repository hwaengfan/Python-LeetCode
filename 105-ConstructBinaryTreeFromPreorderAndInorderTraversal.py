class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        else:
            root = TreeNode(preorder[0])
            midpoint = inorder.index(preorder[0])

            root.left = self.buildTree(
                preorder[1: midpoint + 1], inorder[0: midpoint])
            root.right = self.buildTree(
                preorder[midpoint + 1:], inorder[midpoint + 1:])

            return root
