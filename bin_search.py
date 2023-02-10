def search(arr, targt):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1




arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11

assert search(arr1, target) == 6


