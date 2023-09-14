class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k_(k) {
        for( auto& num : nums )
            add(num);
    }
    
    int add(int val) {
        min_heap_.push(val);
        if(min_heap_.size() > k_)
            min_heap_.pop();
        return min_heap_.top();
    }

private:
    int k_;
    priority_queue<int, vector<int>, greater<int>> min_heap_; // min_heap.top() will give you the minimum element
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */