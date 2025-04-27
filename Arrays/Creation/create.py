class ArrayCreation:
    def __init__(self):
        self.array_size = None
        self.max_attempt = 3  # Increased max attempts for better usability
        self.create_array = []  # Initialize as an empty list
        
    def get_array_size(self):
        attempt = 0
        while attempt < self.max_attempt:
            try:
                # Prompt the user for input
                user_input = input("Enter array size: ").strip()
                
                # Convert the input to an integer
                size = int(user_input)
                
                # Check if the size is greater than 0
                if size > 0:
                    return size  # Return the valid size
                else:
                    print("Array size must be greater than 0.")
            except ValueError:
                # Handle invalid input (non-integer values)
                print("Invalid input. Please enter a positive integer.")
            
            # Increment the attempt counter
            attempt += 1

        # If maximum attempts are exceeded, raise an error or return None
        print(f"Maximum attempts ({self.max_attempt}) exceeded. Exiting...")
        return None
    
    def array_creation(self, size):
        # Create an array of zeros with the given size
        return [0] * size
    
    def user_input_validation(self):
        attempt = 0
        while attempt < self.max_attempt:
            try:
                user_input = input("Enter array value: ").strip()
                if user_input.isdigit():
                    return int(user_input)  # Convert to integer before returning
                else:
                    print("Enter an integer value.")
            except ValueError:
                print("Invalid input. Please provide a valid integer.")
            attempt += 1
        print(f"Maximum attempts ({self.max_attempt}) exceeded. Exiting...")
        return None
    
    def get_array_value(self):
        i = 0
        while i < self.array_size:
            user_value = self.user_input_validation()
            if user_value is not None:
                self.insert_array_value(i, user_value)
                i += 1  # Increment only if input is valid
            else:
                print("Skipping to next index due to invalid input.")
                i += 1  # Increment even if input is invalid to avoid infinite loops
    
    def insert_array_value(self, index, user_input):
        # Insert the value at the specified index
        self.create_array[index] = user_input
    
    def print_array(self):
        return self.create_array
    
    def display(self):
        print("Hi! Let's create an array.")
        self.array_size = self.get_array_size()
        if self.array_size is None:
            print("Array creation failed due to invalid size.")
            return None
        
        # Create the array
        self.create_array = self.array_creation(self.array_size)
        
        # Populate the array with user values
        self.get_array_value()
        
        # Print and return the final array
        arr = self.print_array()
        print("Final array:", arr)
        return arr


if __name__ == "__main__":
    array_create = ArrayCreation()
    array_create.display()