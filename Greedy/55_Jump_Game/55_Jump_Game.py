class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        55. Jump Game
        Medium
        You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.

        Example 1:
        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
        
        Example 2:
        Input: nums = [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
        """
        
        # Starting from the end and working your way backward is a good way to utilize a greedy strategy here. 
        # If at any point you can't find a way to move backward, you'll know you can't reach the beginning and can return false. 
        # Otherwise, if you reach the beginning, you return true.

        n = len(nums)
        last_pos = n-1

        for i in range(n-1, -1, -1):
            if nums[i] + i >= last_pos:
                last_pos = i

        return last_pos == 0
