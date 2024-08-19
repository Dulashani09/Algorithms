def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at the right place
        pi = partition(array, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Example usage
array = [7, 56, 31, 24, 92, 4]
n = len(array)
quick_sort(array, 0, n-1)
print("Sorted array:", array)
