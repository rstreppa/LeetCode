import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;



/** 
Translating the C++ solution into Java is a bit tricky, as Java does not have a direct equivalent of C++'s std::variant. 
However, we can achieve similar functionality using Object types and checking the instance type at runtime. Let's implement a recursive method to flatten a nested list in Java 
*/


public class NestedListFlattener {

    public static List<Object> flatten(List<Object> nestedList) {
        List<Object> flatList = new ArrayList<>();
        flattenHelper(nestedList, flatList);
        return flatList;
    }

    private static void flattenHelper(List<Object> nestedList, List<Object> flatList) {
        for (Object element : nestedList) {
            if (element instanceof List) {
                flattenHelper((List<Object>) element, flatList);
            } else {
                flatList.add(element);
            }
        }
    }

    public static void main(String[] args) {
        List<Object> nestedList = Arrays.asList(
            1, 2, Arrays.asList(3, 4), 
            Arrays.asList(Arrays.asList(5)), 
            Arrays.asList(Arrays.asList(6), Arrays.asList(Arrays.asList(7)))
        );

        List<Object> flatList = flatten(nestedList);
        System.out.println(flatList);
    }
}
