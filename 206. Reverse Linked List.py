# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            # Luu lai node tiep theo truoc khi cat dut lien ket
            next_node = curr.next
            # Dao chieu mui ten tro nguoc lai node phia truoc
            curr.next = prev
            # Di chuyen ca hai con tro len mot buoc
            prev = curr
            curr = next_node
        # Khi curr chay den None, prev se dung o node head moi
        return prev