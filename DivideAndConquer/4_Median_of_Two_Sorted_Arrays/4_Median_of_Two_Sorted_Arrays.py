class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        4. Median of Two Sorted Arrays
        Hard
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        
        The overall run time complexity should be O(log (m+n)).
        
         
        
        Example 1:
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        
        Example 2:
        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
        
        """

        #The problem "Median of Two Sorted Arrays" is a classic example of a divide-and-conquer algorithm problem. 
        # The goal is to find the median of two sorted arrays in logarithmic time, O(log(m+n)).
        # However, the optimal solution actually has a time complexity of O(log(min(m,n))), which is even better than the 
        # O(log(m+n)) constraint mentioned. This can be achieved by using a binary search algorithm on the smaller of the two arrays.
        
        # Main Idea:
        # Partitioning Arrays: The key idea is to partition both arrays into two parts each, say A[0...i-1] and A[i...m-1] for the first array, 
        # and B[0...j-1] and B[j...n-1] for the second array, such that all elements in the left partitions are smaller than all elements 
        # in the right partitions.
        
        # Finding 'i' and 'j': You want to find two indices i and j such that i + j = (m + n + 1) // 2 (for arrays with odd total length) 
        # or i + j = (m + n) // 2 (for arrays with even total length).
        
        # Binary Search: Perform a binary search on the smaller array to find the correct position i, and calculate j using the formula above. 
        # Check the conditions for median using these indices and adjust the binary search accordingly.
        
        # Median Calculation: Once the correct partition is found, you can calculate the median based on the maximum value 
        # on the left side of the partition and the minimum value on the right side.
        
        # By using binary search, you will be able to achieve a time complexity of O(log(min(m,n))), which is optimal for this problem. 

        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        m, n = len(A), len(B)
        half_len = (m + n + 1) // 2  # Corrected this line
        leftA, rightA = 0, m

        while leftA <= rightA:
            i = (leftA + rightA) // 2
            j = half_len - i
            
            if i < m and B[j-1] > A[i]:
                leftA = i + 1
            elif i > 0 and A[i-1] > B[j]:
                rightA = i - 1
            else:
                max_of_left = max(A[i-1] if i > 0 else float('-inf'),
                                  B[j-1] if j > 0 else float('-inf'))

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                min_of_right = min(A[i] if i < m else float('inf'),
                                   B[j] if j < n else float('inf'))

                return (max_of_left + min_of_right) / 2.0
