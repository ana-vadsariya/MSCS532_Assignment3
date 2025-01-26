Time Complexity:

Insert:
Best Case Scenario: Insertion takes O(1) constant time if there is no collision.
Worst Case Scenario: In case of collision it will need to travel along the list giving O(n) linear time for insertion.

Search and Delete:
Best Case Scenario: Value found at the head then takes O(1) constant time.
Worst Case Scenario: In case of needing to travel the list then takes O(n) linear time for searching and deleting.

With uniform hashing it gives O(1+α) where α is the load factor which is the ratio of the number of elements to the number of slots.

Load Factor:
Low load factor contributes to lesser collision hence providing better time complexity and efficieny in the operations.

Strategies for Maintaining a Low Load Factor:
- One way is to resize to double the hash table once it reaches a specific threshold this way all existing keys will be rehashed and it will reduced load factor.
-Other way is to have a hash function that tries to assign keys uniformly rather than unbalancing more values to a key and leaving others empty.
