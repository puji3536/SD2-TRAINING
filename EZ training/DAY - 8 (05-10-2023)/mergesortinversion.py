def inversion_count(arr):
    if len(arr) <= 1:
        return 0
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    inv_count = 0

    inv_count += inversion_count(left)
    inv_count += inversion_count(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv_count += len(left) - i
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inv_count

l = [3, 9, 3, 1, 0]
count = inversion_count(l)
print("Inversion count:", count)
print("Sorted list:", l)