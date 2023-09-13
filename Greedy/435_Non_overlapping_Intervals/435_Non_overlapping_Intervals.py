class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        435. Non-overlapping Intervals
        Medium
        Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

        Example 1:
        Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
        
        Example 2:
        Input: intervals = [[1,2],[1,2],[1,2]]
        Output: 2
        Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
        
        Example 3:
        Input: intervals = [[1,2],[2,3]]
        Output: 0
        Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

        """
        intervals = sorted(intervals, key = lambda x: x[1])
        res = 0
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                res += 1
            else:
                prev_start, prev_end = intervals[i]

        return res
