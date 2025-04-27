# File: search.py

class ArraySearch:
    def __init__(self, array):
        self.array = array  # Accept the array created in ArrayCreation
    
    def linear_search(self, target):
        """Perform linear search for the target value and count the operations."""
        print("Performing Linear Search...")
        operation_count = 0  # Initialize operation counter
        
        for index, value in enumerate(self.array):
            operation_count += 1  # Increment operation count for each comparison
            if value == target:
                print(f"Element {target} found at index {index}.")
                print(f"Total operations performed: {operation_count}")
                return index
        
        print(f"Element {target} not found in the array.")
        print(f"Total operations performed: {operation_count}")
        return -1
    
    def binary_search(self, target):
        """Perform binary search for the target value and count the operations."""
        print("Performing Binary Search...")
        
        # Check if the array is sorted
        if self.array != sorted(self.array):
            print("Binary search requires a sorted array. Please sort the array first.")
            return -1
        
        operation_count = 0  # Initialize operation counter
        left, right = 0, len(self.array) - 1
        
        while left <= right:
            operation_count += 1  # Increment operation count for each iteration
            mid = (left + right) // 2
            if self.array[mid] == target:
                print(f"Element {target} found at index {mid}.")
                print(f"Total operations performed: {operation_count}")
                return mid
            elif self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        print(f"Element {target} not found in the array.")
        print(f"Total operations performed: {operation_count}")
        return -1
    
    def search_menu(self):
        """Display a sub-menu for search operations."""
        while True:
            print("\n--- Search Menu ---")
            print("1. Linear Search")
            print("2. Binary Search")
            print("3. Back to Main Menu")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            print(f'\nArray ======> {self.array}')
            if choice == "1":
                try:
                    target = int(input("Enter the element to search for: "))
                    self.linear_search(target)
                except ValueError:
                    print("Invalid input. Please enter an integer for the target value.")
            
            elif choice == "2":
                try:
                    target = int(input("Enter the element to search for: "))
                    self.binary_search(target)
                except ValueError:
                    print("Invalid input. Please enter an integer for the target value.")
            
            elif choice == "3":
                print("Returning to Main Menu...")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")