#include <iostream>
#include <vector>
#include <variant>
#include <type_traits>


/**
Translating the Python lambda function into C++ requires a bit more effort, as C++ does not natively support the same dynamic typing and recursive lambda expressions as Python. 
Also, C++ does not have a built-in sum function that works on vectors like in Python. We'll use templates for a generic solution that works with any type contained in the nested lists.
Here's how we can implement a recursive function in C++ to flatten a nested list:
*/


template<typename T>
class NestedList {
public:
    using NestedVector = std::vector<std::variant<T, NestedVector>>;

    static std::vector<T> flatten(const NestedVector& nestedList) {
        std::vector<T> flatList;
        flattenHelper(nestedList, flatList);
        return flatList;
    }

private:
    static void flattenHelper(const NestedVector& nestedList, std::vector<T>& flatList) {
        for (const auto& element : nestedList) {
            if (std::holds_alternative<T>(element)) {
                flatList.push_back(std::get<T>(element));
            } else {
                flattenHelper(std::get<NestedVector>(element), flatList);
            }
        }
    }
};

int main() {
    NestedList<int>::NestedVector l = {1, 2, NestedList<int>::NestedVector{3, 4}, NestedList<int>::NestedVector{NestedList<int>::NestedVector{5}}, NestedList<int>::NestedVector{NestedList<int>::NestedVector{6}, NestedList<int>::NestedVector{NestedList<int>::NestedVector{7}}}};
    auto flatList = NestedList<int>::flatten(l);

    for (const auto& elem : flatList) {
        std::cout << elem << " ";
    }

    return 0;
}
