# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        curr = head
        # Duyet qua danh sach khi van con node hien tai va node ke tiep
        while curr and curr.next:
            # Neu phat hien trung lap, bo qua node ke tiep
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                # Neu khong trung lap, di chuyen con tro len 1 buoc
                curr = curr.next
        return head