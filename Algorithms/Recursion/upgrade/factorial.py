def factorial (n: int, array: list) -> int :

    if (len(array) = (n + 1)) : return array[n]
    
    if (n <= 1) : factorial(n, array
    return n * factorial(n-1)

if (__name__ == "__main__") : 
    n = int(input())
    print(factorial(n, []))
