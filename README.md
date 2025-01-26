Clone the repository locally.
Ensure pyhton 3 is installed on your machine
Run the python scripts:
python Randomized_Quick_Sort.py
python Hash_Table.py

Summary for Randomized Quick Sort:
Randomized Quick Sort consistently performs better than Deterministic Quick Sort across various input types. By selecting the pivot randomly, it ensures more balanced splits on average, avoiding the worst-case O(n²). This results in faster sorting times, particularly for sorted or reverse-sorted arrays. Even in cases with repeated values, Randomized Quick Sort maintains reliable and efficient performance, making it the preferred choice for most scenarios due to its consistent O(n log n) time complexity.

Summary for Hash Table:
In hashing with chaining, the time complexity for Insert, Search, and Delete operations depends on the load factor (α), which is the ratio of the number of elements to the number of slots in the hash table. In the best case, when there are no collisions, all operations take O(1) time. However, in the worst case, if a collision occurs and elements need to be traversed in the chain, the time complexity becomes O(n). With uniform hashing, the expected time complexity is O(1 + α). To maintain efficiency, a low load factor is essential, as it reduces collisions and ensures faster operations. Strategies to maintain a low load factor include resizing the hash table (e.g., doubling the size) when the load factor exceeds a threshold and using a well-designed hash function that distributes keys uniformly across the table.



