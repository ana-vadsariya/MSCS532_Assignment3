import random
import time

# Quick Sort Implementation Using Random Pivot Selection
def randomized_quick_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr
    #Randomly select pivot from the array starting at position 0 till the last element
    pivot = arr[random.randint(0, len(arr) - 1)]
    #all the values smaller than pivot goes to left_Side list
    left_side = [x for x in arr if x < pivot]
    #here is the pivot
    pivot_valeu = [x for x in arr if x == pivot]
    #all the values greater than pivot goes to right_Side list
    right_side = [x for x in arr if x > pivot]
    #now we send the left_side + pivot + right_side back to the recursion
    return randomized_quick_sort(left_side) + pivot_valeu + randomized_quick_sort(right_side)

# Quick Sort Implementation Using First Element as Pivot Selection
def deterministic_quick_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr
    #Select first element as the pivot from the array 
    pivot = arr[0]
    #all the values smaller than pivot goes to left_Side list
    left_side = [x for x in arr if x < pivot]
    #here is the pivot
    pivot_valeu = [x for x in arr if x == pivot]
    #all the values greater than pivot goes to right_Side list
    right_side = [x for x in arr if x > pivot]
    #now we send the left_side + pivot + right_side back to the recursion
    return deterministic_quick_sort(left_side) + pivot_valeu + deterministic_quick_sort(right_side)

# Measure execution time of a function 
def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return result, end_time - start_time

def test_sorting_algorithms():
    array_sorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    array_reverse_sorted = [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    array_random = random.sample(range(1, 10000), 1000)  
    array_with_repeated_values = [5,2,3,2,6,5,8,2,10,11,3,5,11,3,4,6,7,2,12]


    #Quick Sort for sorted array
    random_quick_sorted, random_time = measure_time(randomized_quick_sort, array_sorted)
    print("Sorted Array using Randomized Quick Sort") 
    print("Time Taken:", random_time, "seconds")
    print()
        
    #Merge Sort for sorted array
    deterministic_quick_sorted, deterministic_time = measure_time(deterministic_quick_sort, array_sorted)
    print("Sorted Array using Deterministic Quick Sort") 
    print("Time Taken:", deterministic_time, "seconds")
    print()

    #Quick Sort for reverse sorted array
    random_quick_sorted, random_time = measure_time(randomized_quick_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Randomized Quick Sort") 
    print("Time Taken:", random_time, "seconds")
    print()


    #Merge Sort for reverse sorted array
    deterministic_quick_sorted, deterministic_time = measure_time(deterministic_quick_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Deterministic Quick Sort") 
    print("Time Taken:", deterministic_time, "seconds")
    print()

    #Quick Sort for random array
    random_quick_sorted, random_time = measure_time(randomized_quick_sort, array_random)
    print("Sorted Random Array of size 1000 using Randomized Quick Sort") 
    print("Time Taken:", random_time, "seconds")
    print()
        
    #Merge Sort for sorted array
    deterministic_quick_sorted, deterministic_time = measure_time(deterministic_quick_sort, array_random)
    print("Sorted Random Array of size 1000 using Deterministic Quick Sort") 
    print("Time Taken:", deterministic_time, "seconds")
    print()

    #Quick Sort for random array
    random_quick_sorted, random_time = measure_time(randomized_quick_sort, array_with_repeated_values)
    print("Sorted Array with repeated values using Randomized Quick Sort") 
    print("Time Taken:", random_time, "seconds")
    print()
        
    #Merge Sort for sorted array
    deterministic_quick_sorted, deterministic_time = measure_time(deterministic_quick_sort, array_with_repeated_values)
    print("Sorted Array with repeated values using Deterministic Quick Sort") 
    print("Time Taken:", deterministic_time, "seconds")
    print()
 
#used for memory calculation
if __name__ == '__main__':
    test_sorting_algorithms()

