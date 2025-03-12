# from ZADANIE1.tablica import MonitorowanaTablica

from tablica import MonitorowanaTablica


def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1



def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3

        
def merge(L, left, middle, right):
    merged = [None] * (right - left + 1)    
    i, j, k = left, middle + 1, 0

    while i <= middle and j <= right:
        if L[i] <= L[j]:
            merged[k] = L[i]
            i += 1
        else:
            merged[k] = L[j]
            j += 1
        k += 1
    
    while i <= middle:
        merged[k] = L[i]
        i += 1
        k += 1
    
    while j <= right:
        merged[k] = L[j]
        j += 1
        k += 1

    for i in range(len(merged)):
        L[left + i] = merged[i]


def merge_sort(array: MonitorowanaTablica, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        middle = (left + right) // 2

        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)

def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        pivot_index = partition(array, left, right)

        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)


def tim_sort(array: MonitorowanaTablica):
    """Tim Sort implementation."""
    MIN_RUN = 32

    def insertion_sort_subarray(subarray, start, end):
        for i in range(start + 1, end + 1):
            item = subarray[i]
            j = i - 1

            while j >= start and subarray[j] > item:
                subarray[j + 1] = subarray[j]
                j -= 1

            subarray[j + 1] = item

    n = len(array)

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort_subarray(array, start, end)

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            middle = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if middle < right:
                merge(array, left, middle, right)

        size *= 2

algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]
