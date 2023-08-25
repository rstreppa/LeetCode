class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        stack<int> mystack;
        mystack.push(INT_MAX);
        unordered_map<int,int> hash;
        vector<int> res;

        for( const auto& num : nums2 ) {
            while(num > mystack.top()) {
                auto key = mystack.top();
                mystack.pop();
                hash.insert(make_pair(key, num)); 
            }
            mystack.push(num);        
        }

        for( const auto& num : nums1 ) {
            unordered_map<int, int>::const_iterator got = hash.find(num);
            if ( got == hash.end() ) {
                res.push_back(-1);
            } else {
                res.push_back(got->second);  
            }
        }

        return res;
    }
};
