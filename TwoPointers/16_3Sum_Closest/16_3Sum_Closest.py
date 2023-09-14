class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        16. 3Sum Closest
        Medium
        Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
        Return the sum of the three integers.
        You may assume that each input would have exactly one solution.

        Example 1:
        Input: nums = [-1,2,1,-4], target = 1
        Output: 2
        Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        
        Example 2:
        Input: nums = [0,0,0], target = 1
        Output: 0
        Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
        """
        # 1. Sort the array first: O(nlogn)
        # 2. Use a pointer for the first element (let's call it i), and two pointers approach for the remaining elements (let's call them j and k).
        # 3. Move i from 0 to n-3 (inclusive), and for each i, initialize j = i+1 and k = n-1.
        # 4. Calculate sum = nums[i] + nums[j] + nums[k] and update the closest sum you've seen so far based on |target - sum|.
        # 5. Adjust j and k pointers depending on whether sum is less than or greater than target.
        # This approach should get you the answer with O(n^2) time complexity, which is generally acceptable for this kind of problem.

        # Can you do better than O(n^2)? Maybe using a dictionary, like in the two sum problem?
        # In the case of the "3Sum Closest" problem, achieving better than O(n^2) time complexity is difficult, especially because you're looking for the closest sum, 
        # not just any sum that equals the target. The "Two Sum" problem can be solved in O(n) time using a dictionary because you're looking for an exact sum, and you
        # can immediately look up the complement of each number to see if it exists in the array.
        # For the "3Sum Closest" problem, you're not looking for an exact sum but rather the sum closest to the target. 
        # You have to consider almost all possible pairs for each element to determine which one gets you closest to the target.
        # Therefore, the O(n^2) approach is generally considered the most efficient for this particular problem. 
        # If you try to use a data structure like a hash table to speed things up, you'd likely end up needing to check too many possible combinations 
        # to be sure you've found the closest sum, negating any time savings you'd get from the faster lookups.

        # Sort the array
        nums = sorted(nums)

        # Initialize variables
        n    = len(nums)
        res = float('inf')

        for i in range(n-2):
            # Initialize two pointers
            left = i+1
            right = n-1

            # Two pointers technique
            while left < right:
                # Calculate the current sum
                curr = nums[i]+nums[left]+nums[right]
                
                # Update the result if the current sum is closer to the target
                if abs(curr - target) < abs(res - target):
                    res = curr
                
                # Move pointers
                if curr > target:
                    right -= 1
                else:
                    left += 1
        return res
