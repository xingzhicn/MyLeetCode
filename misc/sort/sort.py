def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr

def partition(arr, low, high):
    i = low  # 最初的pivot位置
    pivot = arr[high]  # 取最后一个元素当做pivot
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1  # pivot位置前进1步
    arr[i], arr[high] = arr[high], arr[i]  # 将pivot放到正确的位置并返回位置索引i
    return i


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubbleSort(arr):
    """
    冒泡排序
    :param arr:
    :return:
    """

    for i in range(1, len(arr)):
        flag = False
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag is False:
            return arr
    return arr


def quick_sort(array, left=None, right=None):
    if left == None:
        left = 1
    if right == None:
        right = len(array) - 1
    partation(array, left, right)


def partation(array, left, right):
    base = left
    index = base + 1

    i = index
    while i < right:
        if array[i] > array[base]:
            array[i], array[index] = array[index], array[i]
            index + 1
        i += 1
    array[base], array[index] = array[index], array[base]
    return index


def bubble_sort(array):
    for i in range(1, len(array)):
        flag = True
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return array


def partition1(array, left, right):
    base = left
    index = base + 1
    i = index
    while i <= right:
        if array[i] < array[base]:
            array[i], array[index] = array[index], array[i]
            index += 1
        i += 1
    array[index - 1], array[base] = array[base], array[index - 1]
    return index - 1


def quick_sort1(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        partition1_index = partition1(array, left, right)
        quick_sort1(array, left, partition1_index - 1)
        quick_sort1(array, partition1_index + 1, right)
    return array


def bubble_sort1(array):
    for i in range(1, len(array)):
        flag = True
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return array


if __name__ == '__main__':
    print(bubble_sort([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
    print(bubbleSort([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
    print(quickSort([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
    print(quick_sort1([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
    print(bubble_sort1([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
