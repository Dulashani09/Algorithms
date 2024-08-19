def merge_sort(array):
    if len(array) > 1:
        # Find the middle point
        middle = len(array) // 2

        # Divide the array into two halves
        L = array[:middle]
        R = array[middle:]

        # Sort the first half
        merge_sort(L)

        # Sort the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

# Example usage
array = [7, 56, 31, 24, 92, 4]
merge_sort(array)
print("Sorted array:", array)
