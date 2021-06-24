def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    # 最左边的一个元素为基点pivot
    pivot = left
    # 5,7,13,24,5,67,46,2
    # pivot为5
    # index为7,i为7,从7开始遍历
    index = pivot + 1

    i = index
    while i <= right:
        # 如果当前遍历到的值小于基点
        if arr[i] < arr[pivot]:
            # 交换当前遍历的值跟
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


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


if __name__ == '__main__':
    print(bubbleSort([3, 5, 4, 1, 2, 6]))
    print(bubbleSort([5, 6, 2, 1, 8, 9, 63, 21, 65, 88541, 3854, 31, 21, 84, 31, 848, 6]))
