class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if(Arrays.stream(gas).sum() < Arrays.stream(cost).sum())
            return -1;

        int start_station = 0;
        int current_gas = 0;

        for(int i=0; i<gas.length;i++) {
            current_gas += (gas[i]-cost[i]);
            if(current_gas < 0) {
                start_station = i+1;
                current_gas = 0;
            }
        }
        return start_station;
    }
}
