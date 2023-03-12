class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.arr = self.convertToArr(head)

    def convertToArr(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
