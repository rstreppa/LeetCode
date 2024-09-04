class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> answer;
        
        set<int> h1(nums1.begin(), nums1.end());
        set<int> h2(nums2.begin(), nums2.end());
        
        
        
        vector<int> v1;
        vector<int> v2;


        set_difference(h1.begin(), h1.end(), h2.begin(), h2.end(), inserter(v1, v1.begin()));
        set_difference(h2.begin(), h2.end(), h1.begin(), h1.end(), inserter(v2, v2.begin()));

        answer.push_back(v1);
        answer.push_back(v2);

        return answer;
    }
};