# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current, count = head, 0
        while current != None:
            count, current = count + 1, current.next
        splitSize, extraNodes = divmod(count, k)
        result, current = [], head
        for i in range(k):
            splitHead = current
            for j in range(splitSize + (i < extraNodes) - 1):
                if current:
                    current = current.next
                else:
                    break
            if current:
                current.next, current = None, current.next
            result.append(splitHead)
        return result