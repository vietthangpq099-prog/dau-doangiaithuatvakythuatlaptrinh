class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}  
        for i, num in enumerate(nums):
            # Neu so nay da ton tai va khoang cach vi tri <= k
            if num in seen and i - seen[num] <= k:
                return True 
            # Cap nhat lai vi tri moi nhat cua so nay de cho cac buoc sau kiem tra
            seen[num] = i
        return False