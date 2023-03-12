class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # go to middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        l2 = slow.next
        prev = slow.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        # reorder
        l1, l2 = head, prev
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
