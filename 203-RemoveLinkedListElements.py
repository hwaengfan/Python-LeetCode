class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        trail = None
        while curr:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                    curr = head
                else:
                    trail.next = curr.next
                    curr = trail.next
            else:
                trail = curr
                curr = curr.next
        return head
