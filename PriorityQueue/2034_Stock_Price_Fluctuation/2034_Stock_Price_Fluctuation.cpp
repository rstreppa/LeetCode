class StockPrice {
public:
    StockPrice() {
        latest_timestamp_ = -1;
    }
    
    void update(int timestamp, int price) {
        if (timestamps_.find(timestamp) != timestamps_.end()) {
            int old_price = timestamps_[timestamp];
            price_count_[old_price] -= 1;
        }
        price_count_[price] += 1;
        timestamps_[timestamp] = price;
        latest_timestamp_ = max(latest_timestamp_, timestamp);
        max_heap_.push(price);
        min_heap_.push(price);        
    }
    
    int current() {
        return timestamps_[latest_timestamp_];
    }
    
    int maximum() {
        while(price_count_.find(max_heap_.top()) == price_count_.end() || price_count_[max_heap_.top()] == 0) 
            max_heap_.pop();
        return max_heap_.top();     
    }
    
    int minimum() {
        while(price_count_.find(min_heap_.top()) == price_count_.end() || price_count_[min_heap_.top()] == 0) 
            min_heap_.pop();
        return min_heap_.top();             
    }
private: 
    priority_queue<int> max_heap_;
    priority_queue<int, vector<int>, greater<int>> min_heap_;
    unordered_map<int, int> timestamps_;
    int latest_timestamp_;
    unordered_map<int,unsigned int> price_count_;
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */