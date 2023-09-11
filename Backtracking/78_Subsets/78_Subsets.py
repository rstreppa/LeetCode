class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        78. Subsets
        Medium
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        Example 2:
        Input: nums = [0]
        Output: [[],[0]]
        """
        # backtrack() appends a copy of current to output at the beginning of each call. 
        # This way, each possible subset is included in the output list. 
        # Then, it iterates through the remaining elements, includes or excludes each one, and continues recursively.
        
          
        def backtrack(start=0, current=[]):
            # Append a copy of the current subset to the output
            output.append(current[::])
            
            # Iterate through the remaining elements to include/exclude in the current subset
            for i in range(start, len(nums)):
                # Include the current element
                current.append(nums[i])
                
                # Recur for the next elements
                backtrack(i + 1, current)
                
                # Backtrack to exclude the current element
                current.pop()

        output = []
        backtrack()
        return output
