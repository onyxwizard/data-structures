import random

class ArraySort:
    def __init__(self, array=None):
        self.array = array  # Accept the array created in ArrayCreation
    
    def _validate_array(self):
        """Validate if the array is not empty. If empty, prompt the user to generate a random array."""
        if not self.array:
            print("Array is empty.")
            choice = input("Do you want to generate a random array? (y/n): ").strip().lower()
            if choice == "y":
                size = int(input("Enter the size of the random array: "))
                self.array = [random.randint(1, 100) for _ in range(size)]
                print(f"Generated random array: {self.array}")
            else:
                print("No array provided. Exiting sorting operation.")
                return False
        return True
    
    def _print_sorted_array(self):
        """Print the sorted array."""
        print(f"Sorted array: {self.array}")
    
    def bubble_sort(self):
        """Sort the array using Bubble Sort."""
        if not self._validate_array():
            return
        
        # Core logic for Bubble Sort
        n = len(self.array)
        for i in range(n):
            swap = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swap = True
            if not swap:
                break  # Exit early if no swaps occurred (array is already sorted)
        
        self._print_sorted_array()  # Print the sorted array
    
    def insertion_sort(self):
        """Sort the array using Insertion Sort."""
        if not self._validate_array():
            return
        
        # Core logic for Insertion Sort
        n = len(self.array)
        for index in range(1, n):
            current_element = self.array[index]
            prev = index - 1
            while prev >= 0 and self.array[prev] > current_element:
                self.array[prev + 1] = self.array[prev]
                prev -= 1
            self.array[prev + 1] = current_element
        
        self._print_sorted_array()
    
    def selection_sort(self):
        """Sort the array using Selection Sort."""
        if not self._validate_array():
            return
        
        # Core logic for Selection Sort
        n = len(self.array)
        for i in range(n):
            small = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[small]:
                    small = j
            self.array[i], self.array[small] = self.array[small], self.array[i]
        
        self._print_sorted_array()
    
    def merge_sort(self):
        """Sort the array using Merge Sort."""
        if not self._validate_array():
            return
        
        # Helper function for merge sort
        def merge(arr, l, mid, r):
            left_arr = arr[l:mid + 1]
            right_arr = arr[mid + 1:r + 1]
            
            i = 0  # Index for left_arr
            j = 0  # Index for right_arr
            k = l  # Index for merged array
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        # Helper function for recursive merge sort
        def merge_sort_helper(arr, l, r):
            if l < r:
                mid = (l + r) // 2
                merge_sort_helper(arr, l, mid)
                merge_sort_helper(arr, mid + 1, r)
                merge(arr, l, mid, r)
        
        merge_sort_helper(self.array, 0, len(self.array) - 1)
        self._print_sorted_array()
    
    def quick_sort(self):
        """Sort the array using Quick Sort."""
        if not self._validate_array():
            return
        
        # Helper function for partition
        def partition(arr, left, right):
            pivot = arr[right]
            i = left
            j = right - 1
            
            while i < j:
                while i <= right and arr[i] < pivot:
                    i += 1
                while j >= left and arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i], arr[right] = arr[right], arr[i]
            return i
        
        # Helper function for recursive quick sort
        def quick_sort_helper(arr, left, right):
            if left < right:
                part_pos = partition(arr, left, right)
                quick_sort_helper(arr, left, part_pos - 1)
                quick_sort_helper(arr, part_pos + 1, right)
        
        quick_sort_helper(self.array, 0, len(self.array) - 1)
        self._print_sorted_array()
    
    def sort_menu(self):
        """Display a sub-menu for sorting operations."""
        while True:
            print("\n--- Sorting Menu ---")
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Selection Sort")
            print("4. Merge Sort")
            print("5. Quick Sort")
            print("6. Back to Main Menu")
            
            choice = input("Enter your choice (1/2/3/4/5/6): ").strip()
            
            if choice == "1":
                print("Performing Bubble Sort...")
                self.bubble_sort()
            
            elif choice == "2":
                print("Performing Insertion Sort...")
                self.insertion_sort()
            
            elif choice == "3":
                print("Performing Selection Sort...")
                self.selection_sort()
            
            elif choice == "4":
                print("Performing Merge Sort...")
                self.merge_sort()
            
            elif choice == "5":
                print("Performing Quick Sort...")
                self.quick_sort()
            
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")