def insert_sort(arr) -> list:
        # Core logic for Insert Sort
        n = len(arr)
        for index in range(1,n):
            sorted_val = index - 1
            current_pointer = arr[index]
            
            while sorted_val >=0 and arr[sorted_val] > current_pointer:
                arr[sorted_val+1] = arr[sorted_val]
                sorted_val-=1
            arr[sorted_val+1] = current_pointer
            
        return arr

print(insert_sort([9,6,8,4,2,1]))
print(insert_sort([4,1,3,9,7]))