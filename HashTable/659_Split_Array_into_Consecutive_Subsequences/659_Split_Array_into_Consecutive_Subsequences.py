class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        659. Split Array into Consecutive Subsequences
        Medium

        You are given an integer array nums that is sorted in non-decreasing order.
        Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:
        Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
        All subsequences have a length of 3 or more.
        Return true if you can split nums according to the above conditions, or false otherwise.

        A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing 
        the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

        Example 1:
        Input: nums = [1,2,3,3,4,5]
        Output: true
        Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,5] --> 1, 2, 3
        [1,2,3,3,4,5] --> 3, 4, 5
        
        Example 2:
        Input: nums = [1,2,3,3,4,4,5,5]
        Output: true
        Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
        [1,2,3,3,4,4,5,5] --> 3, 4, 5
        
        Example 3:
        Input: nums = [1,2,3,4,4,5]
        Output: false
        Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.        
        """
        
        # 1 Use a dictionary to keep track of the ending numbers of all the subsequences and how many subsequences end with each number. 
        # This will let you quickly find the shortest subsequence that can be extended.
        
        # 2 Use another dictionary to keep track of the "counts" of each number in the original array, so you can quickly find which numbers 
        # are still available to extend each subsequence.        
        
        count = {}  # Dictionary to hold the count of each number in nums
        tails = {}  # Dictionary to hold the count of subsequences ending with each number

        # Populate count with the frequency of each number in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1


        # Iterate through nums to populate tails
        for num in nums:
            if count[num] == 0:
                continue  # Skip if this number is already used
            
            # Decrease the count for this number, since we're using one instance of it
            count[num] -= 1
            
            # Try to add num to an existing subsequence: if both conditions are true, we can extend a subsequence ending with num - 1 by adding num to it.
            if num - 1 in tails and tails[num - 1] > 0:
                # Remove one subsequence ending with num - 1, we decrement the count of subsequences ending with num - 1 
                # because we're about to extend one of those subsequences, so it will no longer end with num - 1                
                tails[num - 1] -= 1
                tails[num] = tails.get(num, 0) + 1  # Add a new subsequence ending with num
                
            # Else start a new subsequence if possible
            # The condition for starting a new subsequence is that there should be at least one occurrence of both num + 1 and num + 2 remaining in the count dictionary.
            # This is because all subsequences must have a length of 3 or more, according to the problem statement. 
            # If these conditions are met, the new subsequence will be [num, num + 1, num + 2].            
            elif count.get(num + 1, 0) > 0 and count.get(num + 2, 0) > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                tails[num + 2] = tails.get(num + 2, 0) + 1
            
            # Else cannot form a valid subsequence
            else:
                return False

        return True