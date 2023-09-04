class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        260. Single Number III
        Medium
        Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
        Find the two elements that appear only once. You can return the answer in any order.

        You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
        """
        
        # One way to solve it using bit manipulation is as follows:
        # 1 XOR all the numbers in the array. The result will be the XOR of the two numbers that appear only once, say a and b.
        # 2 Find any bit that is set to 1 in the XOR result. This bit must be different between a and b.
        # 3 Use this bit to partition all numbers into two groups: one group with this bit set and another with this bit not set.
        # 4 XOR all the numbers in each group. The two results will be a and b.
        # This algorithm runs in O(n) time and uses O(1) space, meeting the problem's constraints.

        xor_all = 0
        for num in nums:
            xor_all ^= num     # now xor_all is a^b
        
        # find a set bit in xor_all
        diff = 1
        while (xor_all & diff) == 0:
            diff <<= 1
        
        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
