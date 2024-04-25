def factorial (n: int, array: list) -> int :

    if n <= 1 : return array[n]
    else : 
    return n * factorial(n-1)


if (__name__ == "__main__") : 
    n = int(input())
    array = [0, 1]
    print(fibonacci(n, array))
