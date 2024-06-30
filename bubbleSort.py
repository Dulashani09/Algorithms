def bubbleSort(List):

    #Loop through each element in the list except the last one
    for i in range(0,len(List)-1):
        
        # Loop through the list up to the sorted portion
        for j in range(0,len(List)-1-i):

            # Swap the element if the current element is greater than the next element
            if List[j]>List[j+1]:
                List[j],List[j+1]= List[j+1],List[j]
    return List

# Initialize the list to be sorted
List = [23,18,10,86,90,45,58,37]

sorted_list = bubbleSort(List)

# Print the sorted list
print ("Sorted array : " + str(sorted_list))
        
