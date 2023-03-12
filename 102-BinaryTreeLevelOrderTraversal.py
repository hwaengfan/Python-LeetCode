class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()

        if root:
            queue.append(root)

        while queue:
            values = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                values.append(current.val)
            res.append(values)

        return res
