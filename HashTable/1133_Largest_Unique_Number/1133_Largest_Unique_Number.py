def largestUniqueNumber(A):
    ''' 
        Given an array of integers A, return the largest integer that only occurs once.
        If no integer occurs once, return -1.
        
        Example 1:
        Input: [5,7,3,9,4,9,8,3,1]
        Output: 8
        Explanation: 
        The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

        Example 2:
        Input: [9,9,8,8]
        Output: -1
        Explanation: 
        There is no number that occurs only once.
    '''
    d = {}
    for elem in A:
        d[elem] = d.get(elem, 0) + 1
    arr = []
    for k, v in d.items():
        if v == 1:
            arr.append(k)
    return -1 if not arr else sorted(arr)[-1]