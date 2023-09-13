class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        134. Gas Station
        Medium
        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
        You begin the journey with an empty tank at one of the gas stations.
        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
        If there exists a solution, it is guaranteed to be unique
        """
        
        # Intuition Behind the Single Loop:
        
        # 1 Total Gas vs Total Cost: The first thing to note is that if the total amount of gas available is less than the total cost to go from one station to the next, 
        # then it's impossible to complete the circuit. This is easy to understand: you don't have enough gas to go around.

        if sum(gas) < sum(cost):
            return -1

        # 2 Picking the Starting Station: This is the tricky part. Intuitively, whenever you're at a station, and you can't make it to the next one (i.e., current_gas < cost[i]), 
        # it means starting the journey from this station or any station before this wouldn't work. Why? Because if you can't make it from station i to i+1, you wouldn't make 
        # it there starting from i-1, i-2, etc. either, due to a lack of gas. This is the critical insight.

        # 3 Resetting the Journey: Once we realize that station i can't be the starting station (or any before it), we reset our current_gas to 0 and set start_station to i+1, 
        # because the journey must start from some station after i.

        # 4 No Double Loop Needed: The above insight ensures that we don't need a nested loop to try starting from every station. 
        # The greedy choice (resetting the journey when we can't make it to the next station) ensures that if a solution exists, we'll find it efficiently.

        start_station = 0
        current_gas = 0
        
        for i in range(len(gas)):
            current_gas += (gas[i]-cost[i])
            if current_gas < 0:
                start_station = i+1
                current_gas = 0
        return start_station
