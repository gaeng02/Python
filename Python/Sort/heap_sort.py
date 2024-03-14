def heapify (array: list) -> list :
    

def heap_sort (array: list) -> list : 

    heap = Heap(array)
    array = heap.remove_keys()

    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    heap_sort(array)

    print(f"Sorted List")
    print(*array)
