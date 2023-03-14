class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def insert(left, right):
            if left > right:
                return None
            else:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = insert(left, mid - 1)
                root.right = insert(mid + 1, right)
                return root

        return insert(0, len(nums) - 1)
