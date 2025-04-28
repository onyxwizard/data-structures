# File: main.py

from Creation.create import ArrayCreation
from Updation.update import ArrayUpdation
from Access.access import ArrayAccess
from Search.search import ArraySearch
from Traversal.traversal import ArrayTraversal
from Sorting.sort import ArraySort  # Import the new ArraySort class
import random
def main():
    print("--- Welcome to Array Operations ---")
    
    # Default array in case the user skips creation
    default_array = [23, 89, 45, 12, 67]  # Default array: [1, 2, 3, ..., 9]
    array = None  # Initialize as None
    
    while True:
        print("\n--- Menu ---")
        print("1. Create Array")
        print("2. Update Array (Insert/Delete)")
        print("3. Access Array (Index-Based Retrieval)")
        print("4. Search Array")
        print("5. Traverse Array (Forward/Backward)")
        print("6. Sort Array")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == "1":
            # Step 1: Create the array using ArrayCreation
            array_creator = ArrayCreation()
            array = array_creator.display()
            if array is None:
                array = default_array  # Use default array if creation fails
                print(f"Using default array: {array}")
        
        elif choice == "2":
            # Step 2: Perform update operations using ArrayUpdation
            if array is None:
                array = default_array  # Use default array if no array exists
                print(f"No array created. Using default array: {array}")
            
            array_updater = ArrayUpdation(array)
            print("\nPerforming update operations...")
            update_choice = input("Enter 'insert' to insert or 'delete' to delete: ").strip().lower()
            if update_choice == "insert":
                array_updater.insert_element()
            elif update_choice == "delete":
                array_updater.delete_element()
            else:
                print("Invalid update operation. Please enter 'insert' or 'delete'.")
        
        elif choice == "3":
            # Step 3: Perform access operations using ArrayAccess
            if array is None:
                array = default_array  # Use default array if no array exists
                print(f"No array created. Using default array: {array}")
            
            array_accessor = ArrayAccess(array)
            print("\nPerforming index-based retrieval...")
            array_accessor.retrieve_element()
        
        elif choice == "4":
            # Step 4: Perform search operations using ArraySearch
            if array is None:
                array = default_array  # Use default array if no array exists
                print(f"No array created. Using default array: {array}")
            
            array_searcher = ArraySearch(array)
            array_searcher.search_menu()  # Delegate search logic to the ArraySearch class
        
        elif choice == "5":
            # Step 5: Perform traversal operations using ArrayTraversal
            if array is None:
                array = default_array  # Use default array if no array exists
                print(f"No array created. Using default array: {array}")
            
            array_traverser = ArrayTraversal(array)
            array_traverser.traversal_menu()  # Delegate traversal logic to the ArrayTraversal class
        
        elif choice == "6":
            # Step 6: Perform sorting operations using ArraySort
            if array is None:
                array = default_array  # Use default array if no array exists
                print(f"No array created. Using default array: {array}")
            
            array_sorter = ArraySort(array)
            array_sorter.sort_menu()  # Delegate sorting logic to the ArraySort class
        
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()