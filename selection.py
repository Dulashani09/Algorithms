def selection_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

# Example usage
array = [7, 56, 31, 24, 92, 4]
selection_sort(array)
print("Sorted array:", array)
