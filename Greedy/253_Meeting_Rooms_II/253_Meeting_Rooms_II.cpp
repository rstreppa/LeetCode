#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort intervals based on start time using a lambda function
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) -> bool {
        return a[0] < b[0];
    });
    
    // Priority queue to keep track of end times of meetings in rooms
    priority_queue<int, vector<int>, greater<int>> min_heap;
    
    // Initialize by adding the end time of the first meeting
    min_heap.push(intervals[0][1]);
    
    // Iterate through the remaining meetings
    for (int i = 1; i < intervals.size(); ++i) {
        // If the earliest ending meeting ends before or exactly when the next meeting starts
        if (min_heap.top() <= intervals[i][0]) {
            // Free up the room by removing the earliest ending meeting
            min_heap.pop();
        }
        // Add the ending time of the next meeting into the min heap
        min_heap.push(intervals[i][1]);
    }
    
    // The size of the min heap will tell us the minimum number of rooms required
    return min_heap.size();
}
