class ArrayTraversal:
    def __init__(self, array):
        self.array = array  # Accept the array created in ArrayCreation
    
    def forward_traversal(self):
        """Perform forward traversal of the array."""
        if not self.array:
            print("Array is empty. Nothing to traverse.")
            return
        
        print("Forward Traversal:")
        for index, value in enumerate(self.array):
            print(f"Index {index}: {value}")
    
    def backward_traversal(self):
        """Perform backward traversal of the array."""
        if not self.array:
            print("Array is empty. Nothing to traverse.")
            return
        
        print("Backward Traversal:")
        for index in range(len(self.array) - 1, -1, -1):
            print(f"Index {index}: {self.array[index]}")
    
    def traversal_menu(self):
        """Display a sub-menu for traversal operations."""
        while True:
            print("\n--- Traversal Menu ---")
            print("1. Forward Traversal")
            print("2. Backward Traversal")
            print("3. Back to Main Menu")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == "1":
                self.forward_traversal()
            
            elif choice == "2":
                self.backward_traversal()
            
            elif choice == "3":
                print("Returning to Main Menu...")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")