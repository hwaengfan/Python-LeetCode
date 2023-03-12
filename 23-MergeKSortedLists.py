class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergeLists.append(self.mergeTwoLists(l1, l2))
            lists = mergeLists

        return lists[0]

    # merge 2 at a time
    def mergeTwoLists(self, l1, l2):
        sortedList = ListNode()
        head = sortedList

        while l1 and l2:
            if l1.val < l2.val:
                sortedList.next = l1
                l1 = l1.next
            else:
                sortedList.next = l2
                l2 = l2.next
            sortedList = sortedList.next

        if l1:
            sortedList.next = l1
        if l2:
            sortedList.next = l2

        return head.next
