class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Tao mot node gia (dummy node) de lam diem bat dau
        dummy = ListNode(-1)
        current = dummy
        # Duyet khi ca hai danh sach deu con phan tu
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Di chuyen mui kim khau len phia truoc
            current = current.next
        # Noi phan duoi con lai cua danh sach chua het vao cuoi
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        # Tra ve node ngay sau node gia (tuc la head cua danh sach moi)
        return dummy.next