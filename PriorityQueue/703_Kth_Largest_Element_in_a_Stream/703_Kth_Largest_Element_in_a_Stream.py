import heapq 

class KthLargest(object):
    """
    703. Kth Largest Element in a Stream
    Easy
    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Implement KthLargest class:
    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
    
    Example 1:
    Input
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

    Explanation
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8
    """
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []
        
        # Initialize the heap to contain the first k elements from nums
        for num in nums:
            self.add(num)
        


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Your solution is mostly correct but not optimized. Specifically, the add method is inefficient because it uses heapq.nlargest, which takes 
        # O(nlogk) time to find the k-largest elements in an array of n elements.

        # You can improve the efficiency by maintaining a min-heap of size k. This heap will hold the k-largest elements in the stream at all times. 
        # Adding a new element and finding the k-th largest then becomes O(logk).        

        # Add val to the heap
        heapq.heappush(self.min_heap, val)
        
        # If heap size exceeds k, then remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The kth largest element is now at the root of the min-heap
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)