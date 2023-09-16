class StockPrice {
    private PriorityQueue<Integer> max_heap_ = new PriorityQueue<>((o1, o2) -> o2.compareTo(o1));
    private PriorityQueue<Integer> min_heap_ = new PriorityQueue<>();
    private HashMap<Integer, Integer> timestamps_ = new HashMap<Integer, Integer>();
    private Integer latest_timestamp_;
    private HashMap<Integer, Integer> price_count_ = new HashMap<Integer, Integer>();
 
    public StockPrice() {
        latest_timestamp_ = -1;
    }
    
    public void update(int timestamp, int price) {
        if (timestamps_.containsKey(timestamp)) {
            Integer old_price = timestamps_.get(timestamp);
            price_count_.merge(old_price, -1, Integer::sum);
        }
        price_count_.merge(price, 1, Integer::sum);
        timestamps_.put(timestamp, price);
        latest_timestamp_ = Math.max(latest_timestamp_, timestamp);
        max_heap_.add(price);
        min_heap_.add(price);        
        
    }
    
    public int current() {
        return timestamps_.get(latest_timestamp_);
    }
    
    public int maximum() {
        while(!price_count_.containsKey(max_heap_.peek()) || price_count_.get(max_heap_.peek()) == 0) 
            max_heap_.poll();
        return max_heap_.peek();     
        
    }
    
    public int minimum() {
        while(!price_count_.containsKey(min_heap_.peek()) || price_count_.get(min_heap_.peek()) == 0) 
            min_heap_.poll();
        return min_heap_.peek();             
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */