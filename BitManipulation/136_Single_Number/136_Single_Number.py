class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        136. Single Number
        Solved
        Easy
        
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

        You must implement a solution with a linear runtime complexity and use only constant extra space.

        Example 1:
        Input: nums = [2,2,1]
        Output: 1

        Example 2:
        Input: nums = [4,1,2,1,2]
        Output: 4

        Example 3:
        Input: nums = [1]
        Output: 1

        https://hackernoon.com/xor-the-magical-bit-wise-operator-24d3012ed821
        Solution using XOR
        
        Bitwise XOR ( ^ ) like the other operators (except ~) 
        also take two equal-length bit patterns. 
        If both bits in the compared position of the bit patterns are 0 or 1, 
        the bit in the resulting bit pattern is 0, otherwise 1.

        """
        res = 0
        for num in nums:
            res ^= num
        return res