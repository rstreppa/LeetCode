class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        1574. Shortest Subarray to be Removed to Make Array Sorted 
            Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

            Return the length of the shortest subarray to remove.

            A subarray is a contiguous subsequence of the array.

            

            Example 1:

            Input: arr = [1,2,3,10,4,2,3,5]
            Output: 3
            Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
            Another correct solution is to remove the subarray [3,10,4].
            Example 2:

            Input: arr = [5,4,3,2,1]
            Output: 4
            Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
            Example 3:

            Input: arr = [1,2,3]
            Output: 0
            Explanation: The array is already non-decreasing. We do not need to remove any elements.
            

            Constraints:

            1 <= arr.length <= 105
            0 <= arr[i] <= 109
        
        
        :type arr: List[int]
        :rtype: int
        """

        # Optimized Solution Using Two-Pointer

        # The optimized solution leverages a two-pointer technique to find the longest prefix and suffix that are non-decreasing. 
        # The goal is to find the shortest subarray in between these parts that needs to be removed.
        # 1. Find Longest Prefix: Find the longest prefix that is non-decreasing.
        # 2. Find Longest Suffix: Find the longest suffix that is non-decreasing.
        # 3. Calculate Initial Result: Consider removing the prefix or the suffix entirely.
        # 4. Check Middle Part: Use two pointers to find the shortest subarray that can be removed in between the prefix and suffix.
        # The TC of this optimized solution is (O(n) due to the linear scan to find the prefix and suffix and the linear merge process in the end.


        n = len(arr)

        # Find the longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:  # The entire array is already non-decreasing
            return 0

        # Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # The result is to remove the subarray between (left, right)
        res = min(n - left - 1, right)  # Remove either the prefix or the suffix

        # Check if we can remove a middle part
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res


        # Brute Force Solution

        # The brute force solution involves checking every possible subarray to see if removing it results in a non-decreasing array. 
        # This solution is computationally expensive but straightforward.
        # TC: O(n^3) due to the triple nested loops (one for checking each subarray and one for checking if the array is non-decreasing).

        def nonDecreasing(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True

        
        if nonDecreasing(arr):
            return 0
        n = len(arr)
        res = n  # Initialize to the maximum possible length


        for i in range(n):
            for j in range(i, n):
                temp = arr[:i] + arr[j+1:]
                if nonDecreasing(temp):
                    res = min(res, j - i + 1)

        return res



