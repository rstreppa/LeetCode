class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        719. Find K-th Smallest Pair Distance
        Hard
        The distance of a pair of integers a and b is defined as the absolute difference between a and b.
        Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

        Example 1:
        Input: nums = [1,3,1], k = 1
        Output: 0
        Explanation: Here are all the pairs:
        (1,3) -> 2
        (1,1) -> 0
        (3,1) -> 2
        Then the 1st smallest distance pair is (1,1), and its distance is 0.
        
        Example 2:
        Input: nums = [1,1,1], k = 2
        Output: 0
        
        Example 3:
        Input: nums = [1,6,1], k = 3
        Output: 5
        """
        
        # Hint 1 Binary search for the answer. How can you check how many pairs have distance <= X?
        
        # Your idea of creating a list of all pairs and then performing a binary search is a straightforward approach. 
        # However, the time complexity for creating such a list would be O(n^2), and sorting it would take O(n^2 log n^2). 
        # This could be too slow for large inputs, and it also uses O(n^2) additional space.

        # The hint suggests using binary search, but not directly on the list of distances. Instead, it hints at using binary search on the "answer space", 
        # i.e., the possible range of distances. This is because the distances are bound by the minimum and maximum elements in the array.

        # 1 Sort the nums array first. This will let you efficiently count pairs with a certain maximum distance.
        # 2 Use binary search to find the minimum distance d such that there are at least k pairs of elements in nums with distance <= d.
        # 3 To count the number of pairs with distance <= d, you can use two pointers on the sorted array.
        
        # By doing this, you're essentially guessing a possible answer (distance d), checking if it works (if there are enough pairs with distance <= d), 
        # and then adjusting your guess accordingly.

        # The binary search ensures that you'll find the smallest such d, and because each check takes linear time, the overall time complexity would be 
        # O(nlogn) for sorting and O(n log W) for binary search, where W is the range of possible distances. This is a big improvement over O(n^2 logn).


        # 1 Sorting: Sort the nums array. Time complexity: O(nlogn).
        nums  = sorted(nums)
        n     = len(nums)
        left  = 0
        right = abs(nums[n-1] - nums[0])

        # 2 Binary Search: Perform a binary search on the answer space (possible range of distances). 
        # The minimum distance is 0, and the maximum distance is max(nums) - min(nums).
        while left < right:
            mid = left + (right - left) // 2
            # 3 Counting Pairs: For each candidate distance d in the binary search, count how many pairs have a distance <= d. 
            # You can do this efficiently using a two-pointer approach. Time complexity for each candidate: O(n).
            
            # 3a Initialize two pointers i = 0 and j = 1 and a counter variable count = 0.
            i = 0
            j = 1
            count = 0
            # 3b Loop through the sorted array with i starting at 0 and j starting at 1.
            # 3c Count the number of pairs with distance <= mid:
            # If nums[j] - nums[i] <= mid, then increment the counter and move the j pointer to the right.
            # If nums[j] - nums[i] > mid, then move the i pointer to the right.
            # when nums[j] - nums[i] <= mid, you've found one pair (i, j) account for all the other pairs (i, j-1), (i, j-2), ..., (i, i+1) 
            # that also satisfy the condition.

            while i < n:
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1  # Subtract 1 to exclude the pair (i, i)
                i += 1

            # 3d Compare the count:
            # If count >= k, then the distance mid might be too large, and you should search in the smaller half by setting right = mid.
            # If count < k, then the distance mid is too small, and you should search in the larger half by setting left = mid + 1.
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return right