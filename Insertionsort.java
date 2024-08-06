package Data;

public class Insertionsort {	

			// Main method to test the insertion sort algorithm	
			public static void main(String[] args) {

				// Define an array of integers to be sorted
				 int[] array = {5, 34, 90, 13, 77, 52};

		            // Call the insertion sort method to sort the array in ascending order
			        SortAscending(array);
			        System.out.print("Sorted array in ascending order: ");
			        // Print the sorted array
		            for (int i : array) {
			            System.out.print(i + " ");
			        }
			}

		        // Method to perform insertion sort on an array in ascending order
			    public static void SortAscending(int[] array) {
			        int n = array.length;
		            // Traverse through 1 to n-1
			        for (int i = 1; i < n; ++i) {
			            int key = array[i];
			            int j = i - 1;
		                // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
			            while (j >= 0 && array[j] > key) {
			                array[j + 1] = array[j];
			                j = j - 1;
			            }
		                // Place the key element at its correct position in the sorted portion of the array
			            array[j + 1] = key;
			        }
			    }

			}

