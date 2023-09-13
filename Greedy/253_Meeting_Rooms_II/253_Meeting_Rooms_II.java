import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    public static int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) return 0;
        
        // Sort the intervals based on start times
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Priority queue to keep track of end times of meetings in rooms
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        // Initialize by adding the end time of the first meeting
        minHeap.add(intervals[0][1]);
        
        // Iterate through the remaining intervals
        for (int i = 1; i < intervals.length; i++) {
            // If the room due to free up the earliest is free, assign that room to this meeting.
            if (intervals[i][0] >= minHeap.peek()) {
                minHeap.poll();
            }
            
            // Add the current meeting's ending time for tracking.
            minHeap.add(intervals[i][1]);
        }
        
        // The size of the heap tells us the minimum rooms required for all the meetings.
        return minHeap.size();
    }

    public static void main(String[] args) {
        int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println("Minimum number of meeting rooms required: " + minMeetingRooms(intervals));
    }
}
