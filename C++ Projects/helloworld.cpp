#include <iostream> 
#include <vector>

typedef std::vector<std::pair<std::string, int>> pairlist_t;

int main() {
    
    // typedef = reserved keyword used to create an additional name
    //           (alias) for another data type.
    //           New identifier for an existing data type.
    //           Helps with readability and reduces typos.

    // so
    // std::vector<std::pair<std::string, int>> pairlist;
    // becomes
    pairlist_t pairlist;

    return 0;
}