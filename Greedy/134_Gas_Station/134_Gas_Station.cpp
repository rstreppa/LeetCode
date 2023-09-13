class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if(accumulate(gas.begin(), gas.end(), 0) < accumulate(cost.begin(), cost.end(), 0))
            return -1;
        int start_station = 0;
        int current_gas = 0;
        for(unsigned int i=0; i<gas.size(); i++) {
            current_gas += (gas[i]-cost[i]);
            if(current_gas < 0) {
                start_station = i+1;
                current_gas = 0;
            }
        }     
        return start_station;
    }
};
