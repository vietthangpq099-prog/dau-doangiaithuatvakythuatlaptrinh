class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        return sum(1 for h, e in zip(heights, sorted(heights)) if h != e)