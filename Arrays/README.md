# Array Operations Project 🚀

Welcome to the **Array Operations Project** 🎉, a Python-based command-line application that lets you perform various operations on arrays, including creation, updating, accessing, searching, traversing, and sorting. This project is designed to showcase fundamental array operations and sorting algorithms in a fun, interactive, and user-friendly way! 🖥️



## Table of Contents 📋
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Sorting Algorithms](#sorting-algorithms)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)



## Features ✨

The project offers a menu-driven interface with the following operations:

- **Create Array 🆕**: Generate a custom array or use the default array `[23, 89, 45, 12, 67]`.
- **Update Array ✍️**: Insert or delete elements from the array.
- **Access Array 🔍**: Retrieve elements by index.
- **Search Array 🕵️**: Perform search operations (e.g., linear or binary search).
- **Traverse Array 🚶**: Traverse the array forward or backward.
- **Sort Array 🔄**: Sort the array using one of five sorting algorithms:
  - Bubble Sort 🫧
  - Insertion Sort 📌
  - Selection Sort 🎯
  - Merge Sort 🌐
  - Quick Sort ⚡



## Prerequisites 🛠️

To run this project, you need:

- Python 3.x installed on your system 🐍.
- No additional libraries are required, as the project uses only the standard library (e.g., `random` module).



## Installation ⚙️

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/onyxwizard/data-structures.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Arrays
   ```

3. Ensure Python 3 is installed:
   ```bash
   python --version
   ```



## Usage 📖

Run the main script to start the program:
```bash
python main.py
```

Follow the interactive menu to perform array operations:

```
--- Welcome to Array Operations ---
--- Menu ---
1. Create Array
2. Update Array (Insert/Delete)
3. Access Array (Index-Based Retrieval)
4. Search Array
5. Traverse Array (Forward/Backward)
6. Sort Array
7. Exit

Enter your choice (1/2/3/4/5/6/7):
```

Choose an option (1–7) to perform the desired operation. For example, select `6` to access the sorting menu and choose from Bubble, Insertion, Selection, Merge, or Quick Sort. 🧮

### Example: Sorting an Array

- Select `6` from the main menu to enter the sorting menu.
- Choose a sorting algorithm (e.g., `1` for Bubble Sort).
- If no array exists, you can generate a random array or use the default `[23, 89, 45, 12, 67]`.
- The sorted array will be displayed, e.g., `Sorted array: [12, 23, 45, 67, 89]`. ✅



## Sorting Algorithms 🔄

The project implements five classic sorting algorithms in the `sort.py` file, each with unique characteristics:

### Bubble Sort 🫧
- Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
- Optimized to exit early if the array is already sorted.
- **Time Complexity:** O(n²) 😴

### Insertion Sort 📌
- Builds a sorted portion of the array by inserting each element into its correct position.
- Efficient for small or nearly sorted arrays.
- **Time Complexity:** O(n²) 🛠️

### Selection Sort 🎯
- Finds the minimum element in the unsorted portion and places it at the beginning.
- Simple but not efficient for large arrays.
- **Time Complexity:** O(n²) 🔎

### Merge Sort 🌐
- Divides the array into halves, recursively sorts them, and merges the sorted halves.
- Stable and efficient for large datasets.
- **Time Complexity:** O(n log n) 🚀

### Quick Sort ⚡
- Uses a pivot (Hoare's partition scheme) to partition the array and recursively sorts subarrays.
- Highly efficient for large datasets but sensitive to pivot choice.
- **Average Time Complexity:** O(n log n) 🌩️



## File Structure 📁

The project is organized as follows:

```
array-operations/
├── Creation/
│   └── create.py        # Array creation logic
├── Updation/
│   └── update.py        # Array insertion/deletion logic
├── Access/
│   └── access.py        # Array index-based access logic
├── Search/
│   └── search.py        # Array search logic
├── Traversal/
│   └── traversal.py     # Array traversal logic
├── Sorting/
│   └── sort.py          # Array sorting logic (Bubble, Insertion, Selection, Merge, Quick Sort)
├── main.py              # Main script to run the program
└── README.md            # Project documentation
```



## Contributing 🤝

Contributions are welcome! 🎉 To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate comments. 📝



## License 📜

This project is licensed under the **MIT License**. See the `LICENSE` file for details.



Happy coding, and enjoy exploring array operations! 😄  