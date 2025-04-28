def bubble_sort(array) -> list:
        """Sort the array using Bubble Sort."""
        
        # Core logic for Bubble Sort
        n = len(array)
        for i in range(n):
            print(f'The Iteration -> {i} and Array -> {array}')
            swap = False
            for j in range(n - i - 1): # n-i is used to reduce the size of array once sorted
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap = True
            if not swap:
                break  # Exit early if no swaps occurred (array is already sorted)
        
        return array

print(bubble_sort([9,6,8,4,2,1,4]))