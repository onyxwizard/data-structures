def merge_sort(arr) -> list:
        # Core logic for Merge Sort
        if len(arr) > 1:
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            
            merge_sort(left_arr)
            merge_sort(right_arr)
            
            i,j,k = 0,0,0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    j+=1
                k+=1
            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i+=1
                k+=1
            
            while j < len(right_arr):
                arr[k] = right_arr[j]
                k+=1
                j+=1
        
        return arr


print(merge_sort([9,6,8,4,2,1]))
print(merge_sort([4,1,3,9,7]))

"""
    # The problem specifies sorting the subarray from index l to r
    class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:  # Base case: proceed if subarray has more than one element
            mid = (l + r) // 2
            
            # Recursively sort left and right halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)
        
        return arr
    
    def merge(self, arr, l, mid, r):
        # Create temporary arrays for left and right subarrays
        left_arr = arr[l:mid + 1]
        right_arr = arr[mid + 1:r + 1]
        
        i = 0  # Index for left_arr
        j = 0  # Index for right_arr
        k = l  # Index for merged array (start at l)
        
        # Merge left_arr and right_arr back into arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Copy remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
"""