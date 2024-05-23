class Solution {
    public int minSetSize(int[] arr) {
        int n = arr.length;
        HashMap<Integer, Integer> d = new HashMap<>();
        for(int e: arr) {
            if (d.containsKey(e)) 
                d.put(e, d.get(e) + 1);           
            else 
                d.put(e, 1);
        } 
        List<Integer> values = new ArrayList<>();
        for (Integer value : d.values())
            values.add(value);
        Collections.sort(values, Collections.reverseOrder()); 

        int summation = 0;
        int res = 0;
        for(Integer v: values) {
            summation += v;
            res++;
            if(summation >= n/2)
                break;
        }
        return res;
    }
}