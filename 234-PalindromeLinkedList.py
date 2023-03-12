class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        current = slow.next
        prev = slow
        prev.next = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # compare
        l1, l2 = head, prev
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True
