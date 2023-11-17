class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        auto compare = [](int a, int b) 
        {
            int ca = bitset<32>(a).count();
            int cb = bitset<32>(b).count();
            if(ca == cb)
                return a < b;
            return ca < cb;
        };

        sort(arr.begin(), arr.end(), compare);
        return arr; 
    }
};