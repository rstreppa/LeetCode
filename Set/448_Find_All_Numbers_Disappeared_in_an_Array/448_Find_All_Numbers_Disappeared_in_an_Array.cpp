class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> ref(n);
        iota(ref.begin(), ref.end(), 1);
        sort(nums.begin(), nums.end()); 
        
        vector<int> res(n); 
        vector<int>::iterator it = set_difference(ref.begin(), ref.end(), nums.begin(), nums.end(), res.begin());
        res.resize(it-res.begin());  
        return res;
    }
};