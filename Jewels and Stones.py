class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
  
        vip_set = set(jewels)
        return sum(1 for stone in stones if stone in vip_set)