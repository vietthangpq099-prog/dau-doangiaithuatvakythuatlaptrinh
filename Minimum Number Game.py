class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ket_qua = []
        
        for i in range(0, len(nums), 2):
            alice_lay = nums[i]
            bob_lay = nums[i + 1]
            
            ket_qua.append(bob_lay)
            ket_qua.append(alice_lay)
        return ket_qua