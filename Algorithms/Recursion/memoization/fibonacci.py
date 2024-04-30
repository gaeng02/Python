def fibonacci (n: int, array: dict = []) -> int :

    if n <= 2 : return 1
    elif n in array :  return array[n]

    array[n] = fibonacci(n-1, array) + fibonacci(n-2, array)
    return array[n]

if (__name__ == "__main__") : 
    n = int(input())
    array = [0, 1]
    print(fibonacci(n, array))
