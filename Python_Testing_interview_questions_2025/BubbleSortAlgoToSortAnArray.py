arr = [39, 12, 18, 85, 72, 10, 2, 18]


def bubble_sort_array(arr):
    for i in range(0, len(arr)):
        swapped = False
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            break

    return arr


print(bubble_sort_array(arr))
