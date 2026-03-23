class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dem_so = {}
     
        for so in nums:
            if so in dem_so:
                dem_so[so] += 1
            else:
                dem_so[so] = 1
        for so in dem_so:
            if dem_so[so] % 2 != 0:
                return False
        return True