Randomized Quick Sort Runtime:
The runtime for randomized quick sort is O(nlogn). Here we choose the pivot randomly considering that it will divide the array in a balanced way on average. Leaving behind half of the elements (n/2) for next recursion round. Hence it will take total of log n levels of recursion and each will take linear O(n) time for sorting giving us a total of O(nlogn).

Since each level will have two half arrays considering it n/2 for each of them and O(n) for sorting around the pivot we get the recurrence relation as T(n) = 2T(n/2) +O(n) which on solving give us:

So, we can say that T(n/2) ≤ Cn/2 logn/2, here C denotes constant.
So, substituting T(n/2) gives:
T(n) ≤2 (C n/2 logn/2)+O(n)
T(n)≤ C nlogn/2+O(n) 
T(n)≤Cn(logn−1)+O(n)
T(n)≤Cnlogn−Cn+O(n) 
T(n)=O(nlogn)

Result from Running Randomized vs Deterministic Quick Sort:
    Test Case	               Randomized Quick Sort (Time Taken)	Deterministic Quick Sort (Time Taken)
Sorted Array	                    3.36 × 10⁻⁵ seconds             	3.93 × 10⁻⁵ seconds
Sorted Reverse Array               	2.60 × 10⁻⁵ seconds             	3.10 × 10⁻⁵ seconds
Sorted Random Array of size 1000	  0.00193 seconds                     0.00294 seconds
Sorted Array with Repeated Values	1.88 × 10⁻⁵ seconds	                1.03 × 10⁻⁵ seconds

The results show that for sorted, reverse-sorted, and random arrays, the randomized implementation works faster than the deterministic implementation, most likely due to the first element being chosen as the pivot in the deterministic approach, which causes unbalanced array splits. For arrays with repeated values, Deterministic Quicksort shows a notable advantage in this particular case (1.03 × 10⁻⁵ seconds vs. 1.88 × 10⁻⁵ seconds). Overall, Randomized Quicksort demonstrates its theoretical advantage by avoiding the worst-case O(n^2) performance.