class KthLargest {

    private int k_;
    private PriorityQueue<Integer> min_heap_ = new PriorityQueue();

    public KthLargest(int k, int[] nums) {
        k_ = k;
        for(int num : nums)
            add(num);
    }
    
    public int add(int val) {
        min_heap_.add(val);
        if(min_heap_.size() > k_)
            min_heap_.poll();
        return min_heap_.peek();

    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */