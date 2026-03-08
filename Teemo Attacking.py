class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total_time = 0
        for i in range(len(timeSeries) - 1):
            # Khoảng thời gian giữa 2 lần bắn liên tiếp
            time_gap = timeSeries[i+1] - timeSeries[i]
            total_time += min(time_gap, duration)
        total_time += duration
        return total_time