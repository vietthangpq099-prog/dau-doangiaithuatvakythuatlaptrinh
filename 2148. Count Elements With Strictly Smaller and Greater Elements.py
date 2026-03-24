class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lon_nhat = max(nums)
        nho_nhat = min(nums)
        dem = 0
        for so in nums:
            if nho_nhat < so < lon_nhat:
                dem+=1
        return dem
        