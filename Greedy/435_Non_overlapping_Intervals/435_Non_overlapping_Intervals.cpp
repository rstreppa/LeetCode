class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto& left, auto& right) { return left[1] < right[1]; } );
        int res = 0;
        int prev_end = intervals[0][1];
        for(unsigned int i=1; i < intervals.size(); i++) {
            if(intervals[i][0] < prev_end) {
                res++;
            } else {
                prev_end = intervals[i][1];        
            }
        }
        return res;
    }
};
