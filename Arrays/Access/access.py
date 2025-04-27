# File: access.py

class ArrayAccess:
    def __init__(self, array):
        self.array = array  # Accept the array created in ArrayCreation
    
    def _validate_index(self, index):
        """Validate if the index is within bounds."""
        if index < 0 or index >= len(self.array):
            print(f"Invalid index. Index must be between 0 and {len(self.array) - 1}.")
            return False
        return True
    
    def retrieve_element(self):
        """Retrieve an element at a specific index."""
        if not self.array:
            print("Array is empty. Please initialize the array first.")
            return None
        
        try:
            index = int(input("Enter the index to retrieve the element: "))
            if not self._validate_index(index): return None
            element = self.array[index]
            print(f"Element at index {index}: {element}")
            return element
        except ValueError:
            print("Invalid input. Please enter an integer for the index.")
            return None