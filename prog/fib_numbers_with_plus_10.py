def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def add_ten_generator(fib_gen):
    for num in fib_gen:
        yield num + 10

def main():
    n = 10  # Количество чисел Фибоначчи
    fib_gen = fibonacci_generator(n)
    add_ten_gen = add_ten_generator(fib_gen)

    for number in add_ten_gen:
        print(number)

main()