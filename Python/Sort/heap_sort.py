class Heap :
    def __init__ (self, array: list) :
        self.array = array
        self.n = len(array) - 1
        self._make_heap_()

    def remove_keys (self) -> list :
        sorted_array = []
        for i in range (self.n, 0, -1) :
            self.array[i], self.array[1] = self.array[1], self.array[i]
            self.n -= 1
            _sift_down_(1)
            sorted_array.append(self.array[self.n + 1])

        return sorted_array

    def _make_heap_ (self) :
        for index in range ((self.n // 2), 0, -1) :
            _sift_down_(index)

    def _sift_down_ (self, index: int) :
        parent = index
        key = self.array[parent]
        found = False

        while ((2 * parent <= self.n) and (not found)) :
            right = 2 * parent + 1
            left = 2 * parent
            if ((right <= self.n) and (self.array[right] > self.array[left])) :
                max_child = right
            else : max_child = left

            if (key < self.array[max_child]) :
                self.array[parent] = self.array[max_child]
                parent = max_child
                
            else : found = True

        self.array[parent] = key
                    

def heap_sort (array: list) -> list : 

    heap = Heap(array)
    sorted_array = heap.remove_keys()
    array = sorted_array

    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    heap_sort(array)

    print(f"Sorted List")
    print(*array)
