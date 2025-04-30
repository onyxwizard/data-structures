def partition_sort(arr, left, right):
    pivot = arr[right]  # Choose rightmost element as pivot
    i = left   # Left pointer starts before the array
    j = right -1  # Right pointer starts at pivot
    
    while i < j:
        
        while i <= right and arr[i] < pivot:
            i += 1  # Move left pointer until finding element >= pivot
        
        while j >= left and arr[j] > pivot:
            j -= 1  # Move right pointer until finding element <= pivot or hitting left bound
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # Return crossing point (right pointer)
        # Swap elements on wrong sides
    arr[i],arr[right] = arr[right],arr[i]
    return i
    
def quicksort(arr, left, right):
    if left < right:
        part_pos = partition_sort(arr, left, right)
        quicksort(arr, left, part_pos - 1)  # Note: part_pos is inclusive in Hoare
        quicksort(arr, part_pos + 1, right)
    return arr

# Test
arr = [9, 6, 8, 4, 2, 1]
print(quicksort(arr, 0, len(arr) - 1))  # Output: [1, 2, 4, 6, 8, 9]