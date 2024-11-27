#include <iostream> 

namespace first {
    int x = 1;
}
namespace second {
    int x = 2;
}

int main() {
    
    // Namespace provides a solution for preventing name conflicts
    // in large projects. Each entity needs a unique name.
    // A namespace allows for identically named entities 
    // as long as the namespaces are different.

    int x = 0;

    std::cout << x; // outputs 0
    std::cout << first::x; // outputs 1
    std::cout << second::x; // outputs 2

    return 0;
}