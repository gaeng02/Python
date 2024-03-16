def heapify (array: list) -> list :
    

def heap_sort (array: list) -> list : 

    n = len(array)
    heapify(array, n) 

    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    heap_sort(array)

    print(f"Sorted List")
    print(*array)
