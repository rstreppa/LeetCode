class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        496. Next Greater Element I
        Easy
        The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.        
        You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
        For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
        Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
           
        Example 1:      
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1]
        Explanation: The next greater element for each value of nums1 is as follows:
        - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
        - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
        - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
        
        Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4]
        Output: [3,-1]
        Explanation: The next greater element for each value of nums1 is as follows:
        - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
        - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
                
        """


        # You can use a monotonic stack to efficiently find the next greater element for each element in nums2, and then use that
        # information to answer queries about elements in nums1.

        # Here's a brief outline of how to approach this problem using a monotonic stack:

        # Initialize an Empty Stack and a Mapping: Create an empty stack to keep track of elements for which we have not yet found 
        # the next greater element. Also, initialize an empty hash map to store the next greater element for each element in nums2.

        # Iterate Through nums2: Loop through each element in nums2. For each element, use the stack to keep track of elements that are     
        # smaller and are waiting for a greater element to appear.

        # Monotonic Stack: Maintain the stack so that it is decreasing. When you encounter a new element in nums2, 
        # compare it with the top  of the stack. If the new element is greater, it is the 'next greater element' 
        # for the elements in the stack. 
        # Pop those elements and update their next greater element in the hash map.
        # Fill in Answers for nums1: Once you have the next greater elements for all elements in nums2, you can easily fill 
        # in the answers for nums1 by looking up each element in the hash map. If an element doesn't have a next greater element, 
        # you can assign it a value of -1.
        
        # The monotonic stack will help you find the next greater element for each element in nums2 in 
        # O(1) time, making the overall algorithm very efficient.


        stack = [ float('inf') ]
        hash  = {}
        res   = []

        for num in nums2:
            if num > stack[-1]:
                while stack[-1] < num:
                    key = stack.pop()
                    hash[key] = num
            stack.append(num)

        for num in nums1:
            res.append( hash.get( num, -1) )

        return res
