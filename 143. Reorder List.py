# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         #dao nguoc ds
        prev = None
        curr = slow.next
        # Ngat ket noi giua hai nua de tranh tao thanh chu trinh
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        first = head
        second = prev  # prev luc nay la head cua nua sau da duoc dao nguoc
        
        while second:
            # Luu tam cac node tiep theo truoc khi cat dut day noi
            tmp1 = first.next
            tmp2 = second.next
            # Noi cac node cheo nhau (first -> second -> tmp1)
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2