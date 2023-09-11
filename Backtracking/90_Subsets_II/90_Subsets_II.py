class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        90. Subsets II
        Medium
        Given an integer array nums that may contain duplicates, return all possible 
        subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:
        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        
        Example 2:
        Input: nums = [0]
        Output: [[],[0]]
        """

        # To correctly handle duplicates in the list, you should sort the list first 
        # and then make sure to skip over any duplicate values during the backtracking process.

        nums.sort()
        
        def backtrack(start=0, current=[]):
            output.append(current[::])
            
            for i in range(start, len(nums)):
                # Exclude the current element and continue
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Include the current element
                current.append(nums[i])
                
                # Recur for the next elements
                backtrack(i + 1, current)
                
                # Backtrack to exclude the current element
                current.pop()
                
        output = []
        backtrack()
        return output
