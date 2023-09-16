from collections import Counter
import heapq

class StockPrice(object):
    """
    2034. Stock Price Fluctuation 
    Medium
    Topics
    Companies
    Hint
    You are given a stream of records about a particular stock. 
    Each record contains a timestamp and the corresponding price of the stock at that timestamp.

    Unfortunately due to the volatile nature of the stock market, the records do not come in order. 
    Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream 
    correcting the price of the previous wrong record.

    Design an algorithm that:

    Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
    Finds the maximum price the stock has been based on the current records.
    Finds the minimum price the stock has been based on the current records.
    Implement the StockPrice class:

    StockPrice() Initializes the object with no price records.
    void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
    int current() Returns the latest price of the stock.
    int maximum() Returns the maximum price of the stock.
    int minimum() Returns the minimum price of the stock.    
    """
    # First attempt: priority queue on the pairs (timestamp, price) + running min and max
    # The issue is in how you're handling the updates for existing timestamps. You're correctly identifying that you need to update 
    # the price for a given timestamp, but you're not updating the maximum and minimum prices when the update happens.

    # Second attempt: min heap and max heap to keep track of min and max and dictionary to keep track of (timestamp, price) data
    # plus running latest timestamp
    # The problem with the current implementation is that the heaps are not being updated correctly when an existing timestamp's price 
    # is updated. While you remove the old price from the heap, the heap's order is not re-established, 
    # as the heapify operation is not performed.

    # Third attempt: instead of maintaining the max heap and min heap of all prices, you can keep track of the counts of each price 
    # and update them in a similar fashion as you do for timestamps. This way, you can maintain the max and min heap only for 
    # unique prices, reducing the heap size and avoiding the issue of removing elements.

    # The time limit exceeded issue is likely due to the heapify calls in the update method, which has a time complexity of O(n). 
    # Also, removing elements from heaps with remove takes O(n) time, and the heap property is not maintained. 
    # Heapifying after every update is not efficient.

    # Final solution: Use a Counter for price_count to make it easier to increase and decrease the count of prices.
    # Instead of heapifying each time you update the price, you can make sure to manually adjust the heaps only when calling maximum()
    # or minimum(). This avoids the need for a full heapify operation, as you'll only pop the heap's root if it's not in price_count.



    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.timestamps = {}
        self.latest_timestamp = -1
        self.price_count = Counter()
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.timestamps:
            old_price = self.timestamps[timestamp]
            self.price_count[old_price] -= 1

        self.price_count[price] += 1
        self.timestamps[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

        heapq.heappush(self.max_heap, -price)
        heapq.heappush(self.min_heap, price)

    def current(self):
        """
        :rtype: int
        """
        return self.timestamps[self.latest_timestamp]

    def maximum(self):
        """
        :rtype: int
        """
        # -self.max_heap[0] would then be the largest price (in positive form).
        # self.price_count is a dictionary that keeps track of how many times each price appears.
        # This loop continues as long as the largest price (which is -self.max_heap[0]) either:
        # * Does not exist in self.price_count: This could happen if a price was updated and the older price is no longer valid.
        # * Or exists but its count is zero: This means the price was updated to a new value, and this old value is no longer in use.
        # In either of these cases, the loop will pop this largest element from the max heap because it's no longer 
        # a valid candidate for the maximum price.
        # Once the while loop is done, the root of the max heap (-self.max_heap[0]) will be the largest price that is still in use,
        # according to the latest updates.
        while -self.max_heap[0] not in self.price_count or self.price_count[-self.max_heap[0]] == 0:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]

    def minimum(self):
        """
        :rtype: int
        """
        # The same logic applies for the minimum price but using the min heap.
        while self.min_heap[0] not in self.price_count or self.price_count[self.min_heap[0]] == 0:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()