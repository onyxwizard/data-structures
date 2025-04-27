class ArrayUpdation:
    def __init__(self, array):
        self.array = array  # Accept the array created in ArrayCreation
    
    def _validate_position(self, position):
        """Validate if the position is within bounds."""
        if position < 0 or position >= len(self.array):
            print(f"Invalid position. Position must be between 0 and {len(self.array) - 1}.")
            return False
        return True
    
    def insert_element(self):
        """Insert an element at a specific position."""
        if not self.array:
            print("Array is empty. Please initialize the array first.")
            return
        
        try:
            position, value = map(int, input("Enter position and value (space-separated): ").split())
            if not self._validate_position(position): return
            self.array.append(0)  # Add a placeholder at the end
            for i in range(len(self.array) - 1, position, -1):
                self.array[i] = self.array[i - 1]
            self.array[position] = value
            print(f"After insertion: {self.array}")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    
    def delete_element(self):
        """Delete an element at a specific position."""
        if not self.array:
            print("Array is empty. Please initialize the array first.")
            return
        
        try:
            position = int(input("Enter position to delete: "))
            if not self._validate_position(position): return
            for i in range(position, len(self.array) - 1):
                self.array[i] = self.array[i + 1]
            self.array.pop()  # Remove the last element
            print(f"After deletion: {self.array}")
        except ValueError:
            print("Invalid input. Please enter an integer for the position.")