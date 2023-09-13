class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<>() {
            @Override
            public int compare(int[] left, int[] right) {
                return left[1] - right[1];
            }
        });
        int res = 0;
        int prev_end = intervals[0][1]; 
        for(int i=1; i < intervals.length; i++) {
            if(intervals[i][0] < prev_end) {
                res++;
            } else {
                prev_end = intervals[i][1];        
            }
        }
        return res;
    }
}
