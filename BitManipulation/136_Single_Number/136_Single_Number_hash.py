def singleNumber(nums):
    ''' Given a non-empty array of integers nums, every element appears twice except for one. 
        Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
    '''
    d = dict()
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k
        
    return -1