class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        1005. Maximize Sum Of Array After K Negations
        Easy
        Given an integer array nums and an integer k, modify the array in the following way:
        choose an index i and replace nums[i] with -nums[i].
        You should apply this process exactly k times. You may choose the same index i multiple times.
        Return the largest possible sum of the array after modifying it in this way.

        Example 1:
        Input: nums = [4,2,3], k = 1
        Output: 5
        Explanation: Choose index 1 and nums becomes [4,-2,3].
        
        Example 2:
        Input: nums = [3,-1,0,2], k = 3
        Output: 6
        Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
        
        Example 3:
        Input: nums = [2,-3,-1,5,-4], k = 2
        Output: 13
        Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
        """
        nums.sort()
        remain = k                  # Variable to keep track of how many negations are remaining
        n = len(nums)               # Length of the array nums
        
        # Loop to negate the smallest k elements
        for i in range(min(k, n)):  # Make sure we don't go out of bounds
            if nums[i] >= 0:
                break
            nums[i] = -nums[i]
            remain -= 1

        # If we have an odd number of negations left, negate the smallest element
        return sum(nums) - (remain%2)*min(nums)*2
