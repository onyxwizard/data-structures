def selection_sort(arr):
    #code here
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if arr[j]< arr[small]:
                small = j
        arr[i],arr[small] = arr[small],arr[i]
    return arr

print(selection_sort([9,6,8,4,2,1]))
print(selection_sort([4,1,3,9,7]))