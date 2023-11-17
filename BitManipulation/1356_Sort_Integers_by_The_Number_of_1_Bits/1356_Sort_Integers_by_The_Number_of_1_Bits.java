class Solution {
    public int[] sortByBits(int[] arr) {
        // Convert the array to Integer array for custom sorting
        Integer[] integerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);

        // Sort using custom comparator
        Arrays.sort(integerArr, Comparator.comparingInt((Integer i) -> Integer.bitCount(i))
                                          .thenComparingInt(i -> i));

        // Convert back to int array
        return Arrays.stream(integerArr).mapToInt(Integer::intValue).toArray();
    }
}