class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n   = nums.size();
        if(n == 0)
            return 0;
        int i   = 1;
        while(i < n) { 
            if(nums[i] == nums[i-1]) {
                nums.erase(nums.begin()+i);
                n--;
            }
            else
                i++;
        }
        return n;
        
    }
};