# import itertools
import heapq

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        2099. Find Subsequence of Length K With the Largest Sum
        You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

        Return any such subsequence as an integer array of length k.

        A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

        

        Example 1:

        Input: nums = [2,1,3,3], k = 2
        Output: [3,3]
        Explanation:
        The subsequence has the largest sum of 3 + 3 = 6.
        Example 2:

        Input: nums = [-1,-2,3,4], k = 3
        Output: [-1,3,4]
        Explanation: 
        The subsequence has the largest sum of -1 + 3 + 4 = 6.
        Example 3:

        Input: nums = [3,4,3,3], k = 2
        Output: [3,4]
        Explanation:
        The subsequence has the largest sum of 3 + 4 = 7. 
        Another possible subsequence is [4, 3].
        

        Constraints:

        1 <= nums.length <= 1000
        -105 <= nums[i] <= 105
        1 <= k <= nums.length
                
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        # Priority Queue

        # More efficient: use a max heap to keep track of the indices of the k largest elements, then extract them while preserving original order

        # Create a lit of indexed values
        idx_nums = [ (num, i) for i, num in enumerate(nums) ]

        # Use a heap to find the k largest based on their values
        largest_k = heapq.nlargest(k, idx_nums, key = lambda x: x[0])

        # Sort the k largest by their index to keep order
        largest_k.sort(key= lambda x: x[1])

        # Extract the values of the k largest in their original order 
        return [ num for num, _ in largest_k ]





        # Brute Force

        # Generate all possible subsequences of length k and choose those with max sum
        # TC O( C(n,k)*k ) pretty large if n is large

        # max_sum = float('-inf')
        # res     = []

        # Generate all combinations of length k
        # for subseq in itertools.combinations(nums, k):
        #     currsum = sum(subseq)
        #     if currsum > max_sum:
        #         max_sum = currsum
        #         res = subseq

        # return list(res)




