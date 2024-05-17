import heapq 

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int


        1464. Maximum Product of Two Elements in an Array


        Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
        

        Example 1:

        Input: nums = [3,4,5,2]
        Output: 12 
        Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
        Example 2:

        Input: nums = [1,5,4,5]
        Output: 16
        Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
        Example 3:

        Input: nums = [3,7]
        Output: 12
        

        Constraints:

        2 <= nums.length <= 500
        1 <= nums[i] <= 10^3       
        """

        # 1. Use a max-heap (priority queue) to keep track of largest and second largest elements
        # 2. Pop the two largest elements and return desired product 

        # Use a max heap: negate the values to simulate a max heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # pop the two largest elements
        max1 = -heapq.heappop(max_heap)
        max2 = -heapq.heappop(max_heap)

        return (max1-1)*(max2-1)
        
        
        ########################################################
        # Brute Force
        # res = -sys.maxint - 1
        # for i in range(len(nums)):
        #    for j in range(len(nums)):
        #         p = (nums[i]-1)*(nums[j]-1)
        #         if i < j and p > res:
        #             res = p
        # return res