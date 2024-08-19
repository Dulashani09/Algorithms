def heapify(array, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if left < n and array[left] > array[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and array[right] > array[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap

        # Recursively heapify the affected sub-tree
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)

    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0)

# Example usage
array = [7, 56, 31, 24, 92, 4]
heap_sort(array)
print("Sorted array:", array)
