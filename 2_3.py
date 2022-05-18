# Write a program to sort an array of integers.
def sort_in_asc_order(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr

def sort_in_desc_order(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr

arr = [2, 32, 11, 4, 100, 2]
print(sort_in_asc_order(arr))
print(sort_in_desc_order(arr))
