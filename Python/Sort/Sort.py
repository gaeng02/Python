# import Sort

def bubble_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n-1, 0, -1) :
        for j in range (i) :
            if (array[j] > array[j+1]) :
                array[j], array[j+1] = array[j+1], array[j]
                

def exchange_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n) :
        for j in range (i+1, n) :
            if (array[i] > array[j]) :
                array[i], array[j] = array[j], array[i]


def heapify (array: list, index: int, size: int) -> list :
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if ((size > left) and (array[left] > array[largest])) : largest = left
    if ((size > right) and (array[right] > array[largest])) : largest = right
    if (largest != index) :
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, size)    
    
def heap_sort (array: list) -> list : 

    n = len(array)
    for index in range (n//2 -1, -1, -1) : heapify(array, index, n)
    for index in range (n-1, 0, -1) :
        array[0], array[index] = array[index], array[0]
        heapify(array, 0, index)


def insertion_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (1, n) :
        for j in range (i, 0, -1) :
            if (array[j-1] > array[j]) :
                array[j-1], array[j] = array[j], array[j-1]
                
            else : break


def merge_sort (array: list) -> list : 

    n = len(array)
    
    if (n == 1) : return ;

    m = n // 2
    left = array[ : m]
    right = array[m : ]

    merge_sort(left)
    merge_sort(right)
    merge(m, n-m, left, right, array)

def merge (l, r, left, right, array) :

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
