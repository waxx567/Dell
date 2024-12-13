/*
Task Description
interval_map<K,V> is a data structure that associates keys of type K with values of type V. It is designed to be used efficiently in situations where intervals of consecutive keys are associated with the same value. Your task is to implement the assign member function of this data structure, which is outlined below.

interval_map<K, V> is implemented on top of std::map. For more information on std::map, you may refer to cppreference.com.

Each key-value pair (k,v) in interval_map<K,V>::m_map means that the value v is associated with all keys from k (including) to the next key (excluding) in m_map. The member interval_map<K,V>::m_valBegin holds the value that is associated with all keys less than the first key in m_map.

Example: Let M be an instance of interval_map<int,char> where

M.m_valBegin=='A',
M.m_map=={ (1,'B'), (3,'A') },
Then M represents the mapping

...
-2 -> 'A'
-1 -> 'A'
0 -> 'A'
1 -> 'B'
2 -> 'B'
3 -> 'A'
4 -> 'A'
5 -> 'A'
...
The representation in the std::map must be canonical, that is, consecutive map entries must not contain the same value: ..., (3,'A'), (5,'A'), ... is not allowed. Likewise, the first entry in m_map must not contain the same value as m_valBegin. Initially, the whole range of K is associated with a given initial value, passed to the constructor of the interval_map<K,V> data structure.

Key type K

supports copy and move construction, as well as copy and move assignment,
is less-than comparable via operator<,
does not implement any other operations, in particular no equality comparison or arithmetic operators.
Value type V

supports copy and move construction, as well as copy and move assignment,
is equality-comparable via operator==,
does not implement any other operations.
You are given the following source code:
*/

#include <map>

template<typename K, typename V>
class interval_map {
    friend void IntervalMapTest();
    V m_valBegin;
    std::map<K, V> m_map;

public:
    // Constructor associates whole range of K with val
    template<typename V_forward>
    interval_map(V_forward&& val)
        : m_valBegin(std::forward<V_forward>(val)) {}

    // Assign value val to interval [keyBegin, keyEnd).
    // Overwrite previous values in this interval.
    // If !(keyBegin < keyEnd), this designates an empty interval,
    // and assign must do nothing.
    template<typename V_forward>
    void assign(K const& keyBegin, K const& keyEnd, V_forward&& val)
        requires (std::is_same<std::remove_cvref_t<V_forward>, V>::value) {
        
        // Check if the interval is non-empty
        if (!(keyBegin < keyEnd)) return;

        // Erase intervals that overlap with [keyBegin, keyEnd)
        auto itLow = m_map.lower_bound(keyBegin);
        auto itHigh = m_map.lower_bound(keyEnd);

        // Remove affected intervals (we may need to remove entries in the middle)
        m_map.erase(itLow, itHigh);

        // Set the value at keyBegin
        if (itLow == m_map.begin() || (--itLow)->second != val) {
            m_map[keyBegin] = val;
            ++itLow;  // Restore iterator position
        }

        // Set the value at keyEnd
        if (itHigh == m_map.begin() || (--itHigh)->second != val) {
            m_map[keyEnd] = m_valBegin;
        }

        // After insertion, check the neighbors for merging
        if (itLow != m_map.begin() && (--itLow)->second == val) {
            m_map.erase(itLow);
        }

        if (itHigh != m_map.end() && itHigh->second == m_valBegin) {
            m_map.erase(itHigh);
        }
    }
};