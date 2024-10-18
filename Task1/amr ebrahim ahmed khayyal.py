#section 1
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
       
        min_index = i
        print(f"Step {i + 1}: Current array: {arr}")
        
       
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Swapping {arr[min_index]} and {arr[i]}")
        print(f"Array after step {i + 1}: {arr}\n")


arr = [33, 20, 10, 18, 9]
selectionsort(arr)
