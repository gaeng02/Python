# import Sort

def bubble_sort (array: list) -> list : 

    n = len(array)
    comparison, swap = 0, 0
    
    for i in range (n-1, 0, -1) :
        for j in range (i) :
            comparison += 1
            if (array[j] > array[j+1]) :
                swap += 1
                array[j], array[j+1] = array[j+1], array[j]
                
    return comparison, swap

def exchange_sort (array: list) -> list : 

    n = len(array)
    comparison, swap = 0, 0
    
    for i in range (n) :
        for j in range (i+1, n) :
            comparison += 1
            if (array[i] > array[j]) :
                swap += 1
                array[i], array[j] = array[j], array[i]

    return comparison, swap


def heapify (array: list, index: int, size: int, comparison: int, swap: int) -> list :
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if ((size > left) and (array[left] > array[largest])) :
        comparison += 1
        largest = left
        
    if ((size > right) and (array[right] > array[largest])) :
        comparison += 2
        largest = right


    if (largest != index) :
        swap += 1
        array[index], array[largest] = array[largest], array[index]
        comparison, swap = heapify(array, largest, size, comparison, swap)

    return comparison, swap
    
def heap_sort (array: list) -> list : 

    n = len(array)
    comparison, swap = 0, 0
    
    for index in range (n//2 -1, -1, -1) :
        a, b = heapify(array, index, n, comparison, swap)
        comparison, swap = comparison + a, swap + b
        
    for index in range (n-1, 0, -1) :
        swap += 1
        array[0], array[index] = array[index], array[0]
        a, b = heapify(array, 0, index, comparison, swap)
        comparison, swap = comparison + a, swap + b

    return comparison, swap


def insertion_sort (array: list) -> list : 

    n = len(array)
    comparison, swap = 0, 0
    
    for i in range (1, n) :
        for j in range (i, 0, -1) :
            comparison += 1
            if (array[j-1] > array[j]) :
                swap += 1
                array[j-1], array[j] = array[j], array[j-1]
                
            else : break

    return comparison, swap

def merge_sort (array: list) -> list : 

    n = len(array)
    comparison, swap = 0, 0
    
    if (n == 1) : return ;

    m = n // 2
    left = array[ : m]
    right = array[m : ]

    a, b = merge_sort(left)
    comparison, swap = comparison + a, swap + b
    a, b = merge_sort(right)
    comparison, swap = comparison + a, swap + b
    comparison, swap = merge(m, n-m, left, right, array, comparison, swap)

    return comparison, swap

def merge (l, r, left, right, array,comparison: int, swap: int) :

    l, r = l - 1, r - 1
    i, j, k = 0, 0, 0
    
    while ((i <= l) and (j <= r)) :
        if (left[i] < right[j]) : 
            array[k] = left[i]
            i += 1
        elif (left[i] >= right[j]) :
            array[k] = right[j]
            j += 1
        k += 1
        
    while (i <= l) :
        array[k] = left[i]
        i += 1
        k += 1

    while (j <= r) :
        array[k] = right[j]
        j += 1
        k += 1 
    return 

def quick_sort (array: list) -> list : 

    n = len(array)
    _quick_sort(array, 0, n-1) 

def _quick_sort (array: list, low: int, high: int) -> list :
 
    if (low < high) :
        pivot = partition(array, low, high)
        _quick_sort(array, low, pivot-1)
        _quick_sort(array, pivot+1, high)

def partition (array: list, low: int, high: int) -> int :
  
    item = array[low]
    j = low
    for i in range (low+1, high+1) :
        if (array[i] < item) :
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j], array[low] = array[low], array[j]
    return j


def selection_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n) :
        min_index = i
        
        for j in range (i+1, n) :
            if (array[min_index] > array[j]) :
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

if (__name__ == "__main__") :

    '''
    bubble_sort
    exchange_sort
    heap_sort
    insertion_sort
    merge_sort
    quick_sort
    selection_sort
    '''
    array = [5, 4, 3, 2, 1]
    a, b = heap_sort(array)
    
    print(array)
    print(a, b)
