def selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
               
        if min_index != i:         
           
            arr[i],arr[min_index]=arr[min_index],arr[i]

def print_array(arr):
    print(" ".join(map(str, arr))) 

# Main program to test the selection sort
if __name__ == "__main__":
    array = [29, 10, 14, 37, 13]  # Initialize an array of integers to be sorted
    print("Original Array:")
    print_array(array)  # Print the original array

    selection_sort(array)  # Call the selection_sort function to sort the array

    print("Sorted Array:")
    print_array(array)  # Print the sorted array