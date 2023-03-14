class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        trail = None
        while curr:
            if curr != head and curr.val == trail.val:
                trail.next = curr.next
                curr = trail.next
            else:
                trail = curr
                curr = curr.next
        return head
